# 📘 ES6 Promises – Foundations v2.1

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Tasks Summary](#tasks-summary)

---

## Project Overview

This project introduces **ES6 Promises** and asynchronous programming in JavaScript.

You will learn how to manage asynchronous operations using Promises, handle success and failure cases, work with multiple promises, and properly manage errors using `throw` and `try/catch`.
You will also use modern syntax such as `async` / `await`.

This project is part of **Foundations v2.1 – Part 3**.

---

## Learning Objectives

By the end of this project, you should be able to explain, without external help:

### General
- What **Promises** are (how, why, and when to use them)
- How to create and return a Promise
- How to use `then`, `catch`, and `resolve`
- How to use Promise methods (`all`, `race`, `allSettled`)
- How to handle errors with `throw`
- How to use `try` / `catch`
- How the `await` operator works
- How to write and use an `async` function
- How to manage multiple asynchronous operations safely

---

## Requirements

### General
- All files will be interpreted on **Ubuntu 20.04 LTS**
- Using **NodeJS 20.x.x** and **npm 9.x.x**
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files must end with a new line
- A `README.md` file at the root of the project is mandatory
- All files must use the `.js` extension
- All functions must be exported
- Code will be tested using **Jest**
- Code will be analyzed using **ESLint**
- Code must pass all tests and lint checks
- Tests are executed using `npm run test`

---

## Resources

Read or watch:

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An introduction](https://web.dev/articles/promises?hl=fr)
- [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

---

## Tasks Summary

| #  | Task Name                                         | Description                                                       | File                    |
| -- | ------------------------------------------------- | ----------------------------------------------------------------- | ----------------------- |
| 0  | Keep every promise you make                       | Return a basic Promise                                            | `0-promise.js`          |
| 1  | Don't make a promise... if you know you can't     | Resolve or reject a Promise based on a boolean                    | `1-promise.js`          |
| 2  | Catch me if you can!                              | Handle resolved and rejected Promises                             | `2-then.js`             |
| 3  | Handle multiple successful promises               | Resolve multiple Promises using `Promise.all`                     | `3-all.js`              |
| 4  | Simple promise                                    | Return a resolved Promise with user data                          | `4-user-promise.js`     |
| 5  | Reject the promises                               | Return a rejected Promise                                         | `5-photo-reject.js`     |
| 6  | Handle multiple promises                          | Handle resolved and rejected Promises with `Promise.allSettled`   | `6-final-user.js`       |
| 7  | Load balancer                                     | Return the fastest resolved Promise using `Promise.race`          | `7-load_balancer.js`    |
| 8  | Throw an error                                    | Throw an error when dividing by zero                               | `8-try.js`              |
| 9  | Throw error / try catch                           | Handle errors and ensure cleanup logic                             | `9-try.js`              |

---
