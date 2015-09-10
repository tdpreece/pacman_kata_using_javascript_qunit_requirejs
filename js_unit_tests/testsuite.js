requirejs.config({
    // relative to html file
    baseUrl: 'js/lib',
    paths: {
    // relative to baseUrl
        app: '../app',
        app_tests: '../../js_unit_tests',
    //    jquery: 'jquery'
    }
});

requirejs(['app/main']);
