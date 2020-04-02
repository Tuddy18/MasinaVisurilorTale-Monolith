import datetime

from flask_sse import sse

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
        "select * from profile where ProfileId in (select FirstProfileId from matchedcontact where SecondProfileId = {} "
        "union select SecondProfileId from matchedcontact where FirstProfileId = {})".format(profile_id, profile_id))
    profiles = cur.fetchall()
    return render_template("chat.html", profiles=profiles)


@app.route("/chat/<second_person_id>")
def get_chat(second_person_id):
    profile_id = session["accountId"]
    cur = mysql.connection.cursor()
    cur.execute(
        "select * from message where MatchedContactId = (select MatchedContactId from matchedcontact where ((FirstProfileId ={} and SecondProfileId = {}) or (FirstProfileId ={} and SecondProfileId ={}))) order by MessageDateTime desc".format(
            profile_id, second_person_id, second_person_id, profile_id))
    messages = cur.fetchall()
    return jsonify(messages)


@app.route("/message", methods=["POST"])
def add_chat_message():
    data = request.form
    profile_id = session["accountId"]
    cur = mysql.connection.cursor()
    cur.execute(
        "insert into message(MatchedContactId, MessageDateTime, MessageText, MessageOwner) values ({},'{}','{}',{})".format(
            data['MatchedContactId'], datetime.datetime.now(), data['MessageText'], profile_id))
    mysql.connection.commit()
    send_message(data['MessageText'])
    return ""
