function likeProfile(profile_id, liked) {
    $.ajax({
    type: 'POST',
    url: '/match/add',
    data: {
        'profile_id': profile_id,
        'liked': liked
    },
    success: function(msg){
        console.log("Added match: {0} {1}.".format(profile_id, liked))
        location.reload();
    }
   });
}