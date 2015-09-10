define(['jquery'], function (jquery) {
    console.log("app/main loaded OK");
    jquery(document).ready(function () {
        jquery('#game_grid #1-2').html("<div id='pacman'>V</div>");
        jquery('body').on('keypress', function() {
            var pacman = jQuery('#pacman')
            pacman.remove()
            jquery('#game_grid #1-1').append("<div id='pacman'>V</div>");
        })
    });
});
