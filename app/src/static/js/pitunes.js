var player = document.getElementById('player');

$(document).on('click','.row', function(){

    if(player.play()) {
        player.pause();
    }
    var path = $(".path", this).text();
    var id = $(".path", this).attr('id');

    var source = document.getElementById('id_player');
    source.src = path;

    var song = document.getElementById('songTitle'+id).innerHTML;
    var artist = document.getElementById('songArtist'+id).innerHTML;

    document.getElementById('songTitleDisplay').innerHTML = "";
    document.getElementById('songTitleDisplay').innerHTML = song + ' - ' + artist;

    player.load();
    player.play();
});


