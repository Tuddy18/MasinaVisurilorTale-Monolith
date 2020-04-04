let speaking_to;
let matched_contact_id;

function getChatMessages(second_person_id) {
    speaking_to = second_person_id;

    window.setInterval(function () {
        $.get("/chat/" + speaking_to, function (messages) {
            document.getElementById("messages").innerHTML = "";
            for (let i = 0; i < messages.length; i++) {
                document.getElementById("messages").innerHTML += getMessageHtml(messages[i]);
                matched_contact_id = messages[i].MatchedContactId
            }

        });
    }, 2000);

}


function addChatMessage(message) {
    $.post("/message",
        {
            MatchedContactId: matched_contact_id,
            MessageText: message
        }, function () {
            document.getElementById("messages").innerHTML += ' <div class="container_chat">\n' +
                '            <img src="/static/tv.jpg" alt="Avatar" style="width:100%;">\n' +
                '            <p>' + message + '</p>\n' +
                '            <span class="time-right_chat">11:02</span>\n' +
                '        </div>';
            document.getElementById("fname").value = "";
            subscribe()
        }
    );
}

function getMessageHtml(message) {
    const dark_format = ' <div class="container_chat darker_chat" style="width:auto">\n' +
        '            <img src="/static/lada.jpg" alt="Avatar" class="right" style="width:100%;">\n' +
        '            <p>' + message.MessageText + '</p>\n' +
        '            <span class="time-left_chat">11:01</span>\n' +
        '        </div>';
    const white_format = ' <div class="container_chat" style="width:auto">\n' +
        '            <img src="/static/tv.jpg" alt="Avatar" style="width:100%;">\n' +
        '            <p>' + message.MessageText + '</p>\n' +
        '            <span class="time-right_chat">11:02</span>\n' +
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