import datetime

from app import app
from app.config import mysql
from flask import session
from app.user.login import is_logged_in
from flask import request, jsonify
from pywebpush import webpush


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
    try:
        send_web_push(second_profile_id, message)
        return jsonify({'success': 1})
    except Exception as e:
        print("error", e)
        return jsonify({'failed': str(e)})


@app.route('/chat/conversation/<second_person_id>')
def get_conversation(second_person_id):
    cur = mysql.connection.cursor()
    profile_id = session["accountId"]
    cur.execute(
        "select * from message where FirstProfileId = {} and SecondProfileId = {}  order by MessageDateTime desc".format(
            profile_id, second_person_id))
    messages = cur.fetchall()
    return jsonify(messages)


def send_web_push(subscription_information, message_body):
    return webpush(
        subscription_info=subscription_information,
        data=message_body
    )
