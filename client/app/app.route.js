(function () {
    "use strict";
    angular
        .module('app.route', [
            'ngRoute'
        ])
        .config(setRoutes);

    function setRoutes($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true);
        $routeProvider.otherwise({redirectTo: '/home'});
        // TODO: Define all routes here (instead of their modules) to be able to specify the proper ordering and priority of route definitions?
    }

})();
