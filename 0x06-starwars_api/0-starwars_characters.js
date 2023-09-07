#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  printCharacter(characters);
});

const printCharacter = function (url) {
  for (let i = 0; i < url.length; i++) {
    request(url[i], (err, res, body) => {
      if (err) console.log(err);
      if (res.statusCode === 200) console.log(JSON.parse(body).name);
    });
  }
};
