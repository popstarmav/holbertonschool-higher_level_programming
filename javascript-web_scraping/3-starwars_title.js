#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const API_URL = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(API_URL, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error(`Error code: ${response.statusCode}`);
  }
});
