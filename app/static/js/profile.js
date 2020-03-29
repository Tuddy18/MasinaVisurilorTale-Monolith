$( document ).ready(function() {

    $('#feature_to_be_added').on('keypress', function(e){
        if(e.which === 13){
            addFeature( $('#feature_to_be_added').val());
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

//        var chips_container =  $('#feature_to_be_added').parent().parent();
//        var new_chip = $("<div>");
//        new_chip.addClass("chip");
//        new_chip.textContent = feature_text;
//        new_chip.show();
//
//        chips_container.add(new_chip);
    }
   });
}