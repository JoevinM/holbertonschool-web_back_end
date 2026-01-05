# NodeJS Basics

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Table of Tasks](#table-of-tasks)

---

## Project Overview

This project introduces the fundamentals of **Node.js runtime, modules, process APIs, file operations, HTTP servers, and Express routing**.

You will learn how backend JavaScript executes in Node, how asynchronous operations work, and how to build HTTP services using both the native HTTP module and Express.

This project is part of **Foundations v2.1 — Part 3** and contributes to your backend engineering foundations.

---

## Learning Objectives

By the end of this project, you should be able to explain to anyone, **without Google**:

- how to run JavaScript using NodeJS
- how to use NodeJS modules
- how to read files:
  - synchronously
  - asynchronously (Promise-based)
- how to use the `process` API:
  - stdin input
  - command-line arguments
  - environment variables
- how to create a small HTTP server using Node’s HTTP module
- how to create an HTTP server using Express
- how to build advanced Express routes
- how to use ES6 with `babel-node`
- how to use Nodemon for faster development

---

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on **Ubuntu 20.04 LTS**
- Your code must be compliant with **ESLint**
- All files must:
  - end with a new line
  - use `#!/usr/bin/env node` as the first line (when applicable)
- A `README.md` file is mandatory at the root of the project
- Code must follow the **Holberton / ALX style guidelines**
- The length of files will be tested using `wc`
- All modules must have documentation
- All functions must have documentation
  - The documentation must be a full sentence explaining the purpose
  - One-word or vague comments are not allowed
- You must use **ES6 syntax** (no `var`)
- You must use **Node.js LTS 16+**

---

## Resources


Read or watch:
- [Node JS getting started](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [Process API doc](https://node.readthedocs.io/en/latest/api/process/)
- [Child process](https://nodejs.org/api/child_process.html)
- [Express getting started](https://expressjs.com/en/starter/installing.html)
- [Mocha documentation](https://mochajs.org/)
- [Nodemon documentation](https://github.com/remy/nodemon#nodemon)

---

## Table of Tasks

| # | Task name                              | Description                                     | File(s)                |
| - | -------------------------------------- | ----------------------------------------------- | ---------------------- |
| 0 | Executing basic JavaScript with NodeJS | Implement `displayMessage()` printing to STDOUT | `0-console.js`         |
| 1 | Using Process stdin                    | Interactive CLI program reading user input      | `1-stdin.js`           |
| 2 | Read a file synchronously              | Implement `countStudents()` using CSV data      | `2-read_file.js`       |
| 3 | Read a file asynchronously             | Promise-based async CSV reader                  | `3-read_file_async.js` |
| 4 | HTTP server (Node HTTP module)         | Returns `Hello Holberton School!`               | `4-http.js`            |
| 5 | Advanced HTTP server                   | `/students` route + DB stats output             | `5-http.js`            |
| 6 | HTTP server with Express               | Basic Express server on port 1245               | `6-http_express.js`    |
| 7 | Express server with routes             | `/students` route + DB stats                    | `7-http_express.js`    |
| 8 | Organize a complex Express server      | MVC structure + controllers + utils             | `full_server/*`        |

---
