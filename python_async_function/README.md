# 📘 Python – Async

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Tasks Summary](#tasks-summary)

---

## Project Overview

This project introduces asynchronous programming in Python using `async` and `await`.
You will learn how to write coroutines, run them concurrently, schedule tasks, and measure execution time using `asyncio`.

These concepts are essential for building high-performance backend systems that handle multiple I/O operations efficiently.

This project is part of **Foundations v2.1 – Part 2**.

---

## Learning Objectives

By the end of this project, you should be able to explain, without using Google:

- The `async` and `await` syntax
- How to execute an async program using `asyncio`
- How to run multiple coroutines concurrently
- How to create and manage `asyncio.Task` objects
- How to use the `random` module
- How asynchronous programming differs from multithreading

---

## Requirements

### General

- Allowed editors: **vi**, **vim**, **emacs**
- All files will be interpreted/compiled on Ubuntu **20.04 LTS**, Python **3.9**
- All files must:
  - end with a newline
  - start with exactly: `#!/usr/bin/env python3`
  - be executable
  - follow **pycodestyle 2.5.x**
- File length will be checked with `wc`
- A `README.md` at the root is **mandatory**
- All modules must have documentation
  - `python3 -c 'print(__import__("my_module").__doc__)'`
- All functions **and coroutines** must have documentation
- Documentation must be a *sentence describing the purpose*, not a single word
- **Every function must be type-annotated**

---

## Resources

Read or watch:

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

---

## Tasks Summary

| # | Task Name                                      | Description                                                                         | File(s)                       |
|---|------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------|
| 0 | The basics of async                            | Write an async coroutine `wait_random` returning a random delay                    | `0-basic_async_syntax.py`     |
| 1 | Multiple coroutines concurrently               | Write `wait_n` to call `wait_random` n times concurrently                          | `1-concurrent_coroutines.py`  |
| 2 | Measure the runtime                            | Write `measure_time` computing average execution time of `wait_n`                 | `2-measure_runtime.py`        |
| 3 | Async tasks                                    | Write `task_wait_random` returning an `asyncio.Task`                               | `3-tasks.py`                  |
| 4 | Concurrent tasks with Task objects             | Write `task_wait_n` similar to `wait_n` but using `task_wait_random`               | `4-tasks.py`                  |

