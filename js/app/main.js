define(['jquery'], function (jquery) {
    console.log("app/main loaded OK");
    jquery.ready(function () {
        jquery('body').append("<div id='pacman'>V</div>");
    });
});
