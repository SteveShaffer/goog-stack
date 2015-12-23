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
    }

})();
