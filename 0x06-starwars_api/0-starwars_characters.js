#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');

const endpoint = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/';
const url = api + 'films/' + endpoint + '/';
request.get({ url: url }, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    sort(characters);
  }
});

function sort (characters) {
  if (characters.length > 0) {
    request.get({ url: characters.shift() }, function (err, res, body) {
      if (!err) {
        console.log(JSON.parse(body).name);
        sort(characters);
      }
    });
  }
}
