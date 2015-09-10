define(['jquery'], function (jquery) {
    console.log("app/main loaded OK");
    jquery(document).ready(function () {
        jquery('#game_grid #1-2').html("<div id='pacman'>V</div>");
        jquery('body').on('keypress', function(event) {
            var pacman = jQuery('#pacman');
            var column = pacman.parent().index();
            pacman.remove();
            if (event.keyCode == 37) {
                var destination_column = column - 1;
                jquery('#game_grid tr:eq(0) td:eq(' + destination_column + ')').append(pacman);
            }
            else {
                var destination_column = column + 1;
                jquery('#game_grid tr:eq(0) td:eq(2)').append(pacman);
            }
        })
    });
});
