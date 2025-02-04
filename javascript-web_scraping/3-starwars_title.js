#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(apiURL, (error, response, body) => {
    if (error ==  null) {
        const movie = JSON.parse(body);
        console.log(movie.title);
    }
});
