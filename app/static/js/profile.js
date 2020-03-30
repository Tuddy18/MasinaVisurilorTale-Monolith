$( document ).ready(function() {

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
        $('#feature_to_be_added').hide();

        location.reload();
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
        $('#preference_to_be_added').hide();

        location.reload();
    }
   });
}