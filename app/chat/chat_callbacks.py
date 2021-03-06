from flask_socketio import emit, send, join_room
from flask import request, session

from app import socketio

profile_id_to_session = {}

@socketio.on('connect')
def connected():
    print("Client connected on session: ", request.sid)
    profile_id_to_session[str(session["ProfileId"])] = request.sid


@socketio.on("my event")
def handle_custom_event(json):
    print('received event: ' + str(json))


def notify_message_received(second_profile_id):
    if str(second_profile_id) in profile_id_to_session.keys():
        socketio.emit("message_received", room=profile_id_to_session[str(second_profile_id)])

