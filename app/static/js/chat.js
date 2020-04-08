let socketio_host = window.location.hostname + ':' + window.location.port;
$(document).ready(function() {
  var socket = io(socketio_host);
    socket.on('connect', function() {
        console.log("Connected to server");
    });
    socket.on('message_received', function(data) {
        console.log("message received callback fired");
         getChatMessages(speaking_to);
    });
});
let speaking_to;

function getChatMessages(second_person_id) {
    speaking_to = second_person_id;
        $.get("/chat/" + speaking_to, function (messages) {
            document.getElementById("messages").innerHTML = "";
            for (let i = 0; i < messages.length; i++) {
                document.getElementById("messages").innerHTML += getMessageHtml(messages[i]);
            }

        });
}



function addChatMessage(message) {
    if(speaking_to){
         $.post("/message",
        {
            MessageText: message,
            second_profile_id: speaking_to
        }, function () {
            getChatMessages(speaking_to);
        }
    );
    }

}

function getMessageHtml(message) {
    var date_time = new Date(message.MessageDateTime + "+03");
    const dark_format = ' <div class="container_chat darker_chat" style="width:auto">\n' +
        '        <div class="cropped-avatar cropped-avatar-right">\n' +
        '            <img src="' + message.photo_url + '" alt="Avatar" class="avatar-image">\n' +
        '       </div>' +
        '            <p>' + message.MessageText + '</p>\n' +
        '            <span class="time-left_chat">'+ date_time.getHours() + ':' + date_time.getMinutes() + '</span>\n' +
        '        </div>';
    const white_format = ' <div class="container_chat" style="width:auto">\n' +
        '        <div class="cropped-avatar cropped-avatar-left">\n' +
        '            <img src="' + message.photo_url + '" alt="Avatar" class="avatar-image">\n' +
        '       </div>' +
        '            <p>' + message.MessageText + '</p>\n' +
        '            <span class="time-left_chat">'+ date_time.getHours() + ':' + date_time.getMinutes() + '</span>\n' +
        '        </div>';
    if (message.MessageOwner === speaking_to) {
        return dark_format
    } else {
        return white_format
    }
}

function subscribe() {
    var source = new EventSource("{{ url_for('sse.stream') }}");
    source.addEventListener("ola", function (event) {
        var data = JSON.parse(event.data);
        // do what you want with this data
    }, false);
}