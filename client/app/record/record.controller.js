(function () {
    "use strict";
    angular
        .module('record.controller', [
            'record.service'
        ])
        .controller('RecordController', Controller);

    function Controller ($routeParams, Record) {
        var vm = this;
        vm.record = Record.get({recordType: $routeParams.recordType, recordId: $routeParams.recordId});  // TODO: Just pass $routeParams?
    }

})();
