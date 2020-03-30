import datetime

from flask_sse import sse

from app import app
from app.config import mysql
from flask import session
from flask import request, jsonify

app.register_blueprint(sse, url_prefix='/stream')


@app.route('/send/<first_person_id>/<second_person_id>')
def send_message(first_person_id, second_person_id):
    sse.publish(get_conversation_from_db(first_person_id, second_person_id),
                type="{}/{}".format(first_person_id, second_person_id))
    return "Message sent!"


@app.route('/chat', methods=['GET', 'POST'])
def get_all_conversations():
    if request.method == 'GET':
        return get_chat_conversations()
    if request.method == 'POST':
        message = request.get_json()
        return add_chat_message(message)


def get_chat_conversations():
    cur = mysql.connection.cursor()
    profile_id = session["accountId"]
    cur.execute(
        "select * from message where FirstProfileId = {} or SecondProfileId = {}".format(profile_id, profile_id))
    messages = cur.fetchall()
    conversation_user = set()
    for message in messages:
        conversation_user.add(str(message["FirstProfileId"]))
        conversation_user.add(str(message["SecondProfileId"]))
    conversation_user.remove(str(profile_id))
    conversation_user_profile = {}
    if conversation_user.__len__() > 0:
        cur.execute("select * from profile where ProfileId in ({})".format(",".join(conversation_user)))
        conversation_user_profile = cur.fetchall()
    return jsonify(conversation_user_profile)


def add_chat_message(message):
    profile_id = session["accountId"]
    second_profile_id = message['SecondProfileId']
    # message_text = message['MessageText']
    cur = mysql.connection.cursor()
    cur.execute("insert into message(FirstProfileId, SecondProfileId, MessageDateTime) values ({},{}, '{}')".format(
        profile_id, second_profile_id, str(datetime.datetime.now())))
    mysql.connection.commit()
    return ""


@app.route('/chat/conversation/<second_person_id>')
def get_conversation(second_person_id):
    profile_id = session["accountId"]
    messages = get_conversation_from_db(profile_id, second_person_id)
    return jsonify(messages)


def get_conversation_from_db(first_person_id, second_person_id):
    cur = mysql.connection.cursor()
    cur.execute(
        "select * from message where FirstProfileId = {} and SecondProfileId = {}  order by MessageDateTime desc".format(
            first_person_id, second_person_id))
    messages = cur.fetchall()
    return messages
