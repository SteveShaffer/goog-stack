(function () {
    "use strict";
    angular
        .module('record.route', [
            'ngRoute'
        ])
        .config(setRoutes);

    function setRoutes($routeProvider) {
        $routeProvider
            .when('/:recordType/:recordId', {  // TODO: How to deal with this matching types registered with other modules?  .otherwise?
                controller: 'RecordController',
                controllerAs: 'vm',
                templateUrl: 'app/record/record.tpl.html'
            });
    }

})();
