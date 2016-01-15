(function () {
    "use strict";
    angular
        .module('home.controller', [])
        .controller('HomeController', Controller);

    function Controller ($route) {
        var vm = this;
        vm.routes = $route.routes;
    }

})();
