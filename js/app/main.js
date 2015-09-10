define(['jquery'], function (jquery) {
    console.log("app/main loaded OK");
    jquery(document).ready(function () {
        jquery('#game_grid #1-2').html("<div id='pacman'>V</div>");
        jquery('body').on('keypress', function(event) {
            var pacman = jQuery('#pacman')
            pacman.remove()
            if (event.keyCode == 37) {
               jquery('#game_grid #1-1').append(pacman);
            }
            else {
               jquery('#game_grid #1-3').append(pacman);
            }
        })
    });
});
