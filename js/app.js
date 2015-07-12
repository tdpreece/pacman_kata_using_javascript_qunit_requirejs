requirejs.config({
    // relative to html file
    baseUrl: 'js/lib',
    paths: {
    // relative to baseUrl
        app: '../app',
    //    jquery: 'jquery'
    }
});

requirejs(['app/main']);
