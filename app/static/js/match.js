function likeProfile(profile_id, liked) {
    $.ajax({
    type: 'POST',
    url: '/match/add',
    data: {
        'profile_id': profile_id,
        'liked': liked
    },
    success: function(msg){
        location.reload(true);
    }
   });
}