(function () {
    "use strict";
    angular
        .module('app.route', [
            'ngRoute'
        ])
        .config(rootRoutes);

    function rootRoutes($routeProvider) {
        // TODO: html5mode?
        $routeProvider.otherwise({redirectTo: '/home'});
    }

})();
