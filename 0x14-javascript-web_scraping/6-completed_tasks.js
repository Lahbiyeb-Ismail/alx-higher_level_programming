#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

const getCompletedTasks = () => {
  request.get(url, (err, response) => {
    if (err) {
      console.log(err);
    }

    const todos = JSON.parse(response.body);

    const completedTasks = {};

    for (let i = 0; i < todos.length; i++) {
      const userId = todos[i].userId;
      if (todos[i].completed && completedTasks[userId]) {
        completedTasks[userId] += 1;
      } else if (todos[i].completed && !completedTasks[userId]) {
        completedTasks[userId] = 1;
      }
    }

    console.log(completedTasks);
  });
};

getCompletedTasks();
