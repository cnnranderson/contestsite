// Generated by CoffeeScript 1.7.1
var DEBUG, GradingMain, angularApp;

DEBUG = 0;

angularApp = angular.module("Grading", []).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  return $interpolateProvider.endSymbol(']]');
});

angularApp.factory("api", function($http, $q) {
  return {
    test: function() {
      return console.log("test!");
    },
    getUngradedResults: function(successFunc) {
      return $http.get('/api/v1/ungradedresult?format=json').then(successFunc, function(response) {
        return $q.reject(response.data);
      });
    }
  };
});

angularApp.controller('Main', GradingMain = (function() {
  function GradingMain($scope, api) {
    this.$scope = $scope;
    this.api = api;
    console.log("instantiated");
    this.$scope.solutions = [
      {
        command: 'test'
      }, {
        command: 'test234'
      }
    ];
    this.load();
  }

  GradingMain.prototype.load = function() {
    console.log("load called");
    return this.api.getUngradedResults((function(_this) {
      return function(response) {
        console.log(response.data.objects);
        _this.$scope.solutions = response.data.objects;
        return DEBUG = _this.solutions;
      };
    })(this));
  };

  GradingMain.prototype.setSelected = function(solution) {
    console.log("selected!");
    return console.log(solution);
  };

  return GradingMain;

})());
