(function () {
    "use strict";
    angular
        .module('record.service', [])
        .factory('Record', Factory);

    function Factory ($resource) {
        return $resource('/api/records/:recordType/:recordId');
    }

})();
