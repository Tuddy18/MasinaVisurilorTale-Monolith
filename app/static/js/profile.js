$( document ).ready(function() {
    $("#profile_description").blur(function(e){
        updateDescription( $("#profile_description").first().text());
    });
    $('#photo_to_be_added').on('keypress', function(e){
        if(e.which === 13){
            addPhoto( $('#photo_to_be_added').val());
        }
    });

    $('#feature_to_be_added').on('keypress', function(e){
        if(e.which === 13){
            addFeature( $('#feature_to_be_added').val());
        }
    });


    $('#preference_to_be_added').on('keypress', function(e){
        if(e.which === 13){
            addPreference( $('#preference_to_be_added').val());
        }
    });
});

function addChip($chips_parent, text, remove_function){
        var node = document.createElement("div");                 // Create a <li> node
        node.classList.add("chip");
        var textnode = document.createTextNode(text);         // Create a text node
        node.appendChild(textnode);

        var close_btn = document.createElement("span");
        close_btn.classList.add("closebtn");
        close_btn.onclick = function() { remove_function(close_btn, text); };
        close_btn.innerHTML = "&times;";         // Create a text node
        node.appendChild(close_btn);

        $chips_parent = $chips_parent.append(node);
}

function updateDescription(new_description){
     $.ajax({
    type: 'POST',
    url: '/profile/update-description',
    data: {
        'description_text': new_description
    },
    success: function(msg){
        console.log('Updated description: ' + new_description);
    }
   });
}
function addPhoto(photo_url){
    $.ajax({
    type: 'POST',
    url: '/profile/add-photo',
    data: {
        'photo_url': photo_url
    },
    success: function(msg){
        console.log('Added Photo: ' + photo_url);

        var $carousel_inner = $('#photo_to_be_added').parent().parent();

        var node = document.createElement("div");
        node.classList.add("item");

        var image = document.createElement("img");
        image.classList.add("profile-image");
        image.src = photo_url;
        image.style = "width: 100%;";
        node.appendChild(image);

        $carousel_inner = $carousel_inner.append(node);

        $('#photo_to_be_added').hide();
        $('#photo_to_be_added').val('');
    }
   });
}

function removePhoto(){

    var photo_url_to_remove = $(".item.active").children("img").attr("src");

    $.ajax({
    type: 'POST',
    url: '/profile/remove-photo',
    data: {
        'photo_url' : photo_url_to_remove
    },
    success: function(msg){
        console.log('Removed photo Photo');

        $(".item.active").remove()
        $(".item").first().addClass("active")
    }
   });
}



function removeFeature(clicked_button, feature_text) {
//    $.ajax({url:'/profile/remove-chip' + feature_name});

    $.ajax({
    type: 'POST',
    url: '/profile/remove-feature',
    data: {
        'feature_text': feature_text
    },
    success: function(msg){
        console.log('Deleted Feature: ' + feature_text);
        clicked_button.parentElement.style.display='none';
    }
});
}


function addFeature(feature_text) {
    $.ajax({
    type: 'POST',
    url: '/profile/add-feature',
    data: {
        'feature_text': feature_text
    },
    success: function(msg){
        console.log('Added Feature: ' + feature_text);

        var $chips_parent = $('#feature_to_be_added').parent().parent();

        addChip($chips_parent, feature_text, removeFeature);

        $('#feature_to_be_added').hide();
        $('#feature_to_be_added').val('');
    }
   });
}

function removePreference(clicked_button, preference_text) {
//    $.ajax({url:'/profile/remove-chip' + preference_name});

    $.ajax({
    type: 'POST',
    url: '/profile/remove-preference',
    data: {
        'preference_text': preference_text
    },
    success: function(msg){
        console.log('Deleted Preference: ' + preference_text);
        clicked_button.parentElement.style.display='none';
    }
});
}


function addPreference(preference_text) {
    $.ajax({
    type: 'POST',
    url: '/profile/add-preference',
    data: {
        'preference_text': preference_text
    },
    success: function(msg){
        console.log('Added Preference: ' + preference_text);
        $chips_parent = $('#preference_to_be_added').parent().parent();

        addChip($chips_parent, preference_text, removePreference);

        $('#preference_to_be_added').hide();
        $('#preference_to_be_added').val('');

    }
   });
}