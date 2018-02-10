'use strict';
angular.module('app', ['ngMap'])
  .controller('locatorController', function($scope, $timeout, NgMap) {
    $scope.markers = []
    $scope.path = []
    $scope.path.push(["28.4357","77.0984221"])
    $scope.path.push(["28.4357","77.0984221"])
    $scope.path.push(["28.4357","77.0984221"])

    $scope.allShapes = [
    {name: "polyline", path: [[40.74,-74.18],[40.64,-74.10],[40.54,-74.05],[40.44,-74]]},
    {name: "polygon", paths: [[40.74,-74.18],[40.64,-74.18],[40.84,-74.08],[40.74,-74.18]]},
    {name: "rectangle", bounds: [[40.74,-74.18], [40.78,-74.14]]},
    {name: "circle", center:[40.70,-74.14], radius:4000}
  ];

      // $http.get("flight_info.txt").success(function (response) { $scope.flights=response; });

      // for (var key in $scope.flights) {
      //   var flight_number = key
      //   var flight_info = dict[key];
                         
      // }
      $scope.markers = [
      {
        "id": "1",
        "pos": ["28.4357","77.0984221"],
        "flight_name":"inf=digo", 
        "icon": "dot.png"
      }, {
        "id": "2",
        "latitude": "39.15",
        "longitude": "-98.45"
      }, {
        "id": "3",
        "latitude": "39.25",
        "longitude": "-97.95"
      },
    ]



  })
  .controller('templateController',function(){});