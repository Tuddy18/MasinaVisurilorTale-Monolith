import datetime

from app.chat.chat_callbacks import notify_message_received
from app.config import mysql
from flask import session, request
from flask import jsonify, render_template
from app import app


@app.route('/chat')
def get_all_conversations():
    return get_conversations()


def get_conversations():
    cur = mysql.connection.cursor()
    profile_id = session["accountId"]
    cur.execute(
        "select * from profile where ProfileId in ("
        "(select FirstProfileId from matchedcontact where SecondProfileId = {} and  "
        "FirstProfileLike = 1 and SecondProfileLike = 1)"
        "union "
        "(select SecondProfileId from matchedcontact where FirstProfileId = {} and "
        "FirstProfileLike = 1 and SecondProfileLike = 1))".format(profile_id, profile_id))
    profiles = cur.fetchall()

    for profile in profiles:
        second_profile_photo = "https://cdn.iconscout.com/icon/free/png-256/car-disconnected-lost-connection-laptop-device-29510.png"
        result = cur.execute("SELECT Url from Photo where ProfileId = {}".format(profile["ProfileId"]))
        if result > 0:
            second_profile_photo = cur.fetchone()["Url"]
        profile["photo"] = second_profile_photo
    return render_template("chat.html", profiles=profiles)


@app.route("/chat/<second_person_id>")
def get_chat(second_person_id):
    profile_id = session["ProfileId"]
    cur = mysql.connection.cursor()

    first_profile_photo = "https://cdn.iconscout.com/icon/free/png-256/car-disconnected-lost-connection-laptop-device-29510.png"
    result = cur.execute("SELECT Url from Photo where ProfileId = {}".format(profile_id))
    if result > 0:
        first_profile_photo = cur.fetchone()["Url"]

    second_profile_photo = "https://cdn.iconscout.com/icon/free/png-256/car-disconnected-lost-connection-laptop-device-29510.png"
    result = cur.execute("SELECT Url from Photo where ProfileId = {}".format(second_person_id))
    if result > 0:
        second_profile_photo = cur.fetchone()["Url"]

    result = cur.execute("select MatchedContactId from matchedcontact where "
        "((FirstProfileId ={} and SecondProfileId = {}) or "
        "(FirstProfileId ={} and SecondProfileId ={}))"
        .format(profile_id, second_person_id, second_person_id, profile_id))
    if result > 0:
        session["MatchedContactId"] = cur.fetchone()["MatchedContactId"]

        cur.execute("select * from message where MatchedContactId = {} "
                    "order by MessageDateTime".format(session["MatchedContactId"]))
        messages = cur.fetchall()

        for message in messages:
            message["photo_url"] = first_profile_photo if message["MessageOwner"] == profile_id else second_profile_photo
        return jsonify(messages)



@app.route("/message", methods=["POST"])
def add_chat_message():
    data = request.form
    profile_id = session["accountId"]
    cur = mysql.connection.cursor()
    cur.execute(
        "insert into message(MatchedContactId, MessageDateTime, MessageText, MessageOwner) values ({},'{}','{}',{})".format(
            session['MatchedContactId'], datetime.datetime.now(), data['MessageText'], profile_id))
    mysql.connection.commit()
    notify_message_received(data["second_profile_id"])
    return ""
