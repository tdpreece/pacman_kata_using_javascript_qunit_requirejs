define(['jquery'], function (jquery) {
    console.log("app/main loaded OK");
    jquery(document).ready(function () {
        jquery('body').append("<div id='pacman'>V</div>");
    });
});
