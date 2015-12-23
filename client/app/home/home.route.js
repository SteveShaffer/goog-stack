(function () {
    "use strict";
    angular
        .module('home.route', [
            'ngRoute'
        ])
        .config(setRoutes);

    function setRoutes($routeProvider) {
        $routeProvider
            .when('/home/', {
                controller: 'HomeController',
                controllerAs: 'vm',
                templateUrl: 'app/home/home.tpl.html'
            });
    }

})();
