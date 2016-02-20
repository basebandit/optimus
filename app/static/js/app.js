/**
 * Created by mars on 2/19/16.
 */
angular.module('optimusApp', ['ui.router', 'ngResource', 'optimusApp.controllers', 'optimusApp.services']);
angular.module('optimusApp').config(function ($stateProvider) {
    $stateProvider.state('movies', {
        //State for showing all movies currently stocked
        url: '/movies',
        templateUrl: 'templates/movies.html',
        controller: 'MovieListController'
    }).state('viewMovie', {
        //State for showing a single movie
        url: '/movies/:id/view',
        templateUrl: 'templates/movie-view.html',
        controller: 'MovieViewController'
    }).state('newMovie', {
        //State for adding a new movie
        url: '/movies/new',
        templateUrl: 'templates/movie-add.html',
        controller: 'MovieCreateController'
    }).state('editMovie', {
        //State for updating an existing movie
        url: '/movies/:id/edit',
        templateUrl: 'templates/movie-edit.html',
        controller: 'MovieEditController'
    });
});