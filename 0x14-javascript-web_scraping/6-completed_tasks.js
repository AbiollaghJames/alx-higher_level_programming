#!/usr/bin/node

const request = require('request');
const API_URL = process.argv[2];

request(API_URL, function (err, response, body) {
  if (err) {
    throw new Error(err);
  } else if (reponse.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = new Map();

    todos.forEach ((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
	completedTasks.set(userId, (completedTasks.get(userId) || 0) + 1);
      }
    });
    for (const [userId, count] of completedTasks) {
      console.log(${userId}, ${count});
    }
    });
  } else {
    console.log(response.statusCode);
  }
});
