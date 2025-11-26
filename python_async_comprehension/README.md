# 📘 Python – Async Comprehension

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Tasks Summary](#tasks-summary)

---

## Project Overview

This project introduces **asynchronous generators**, **async comprehensions**, and **typing asynchronous generators** using Python's `asyncio` framework.

You will learn how to:
- write asynchronous generators,
- iterate over them using async comprehensions,
- execute async comprehensions concurrently,
- measure execution time of asynchronous workloads.

These concepts build on top of the async fundamentals and are used to optimize applications that need to stream data asynchronously.

This project is part of **Foundations v2.1 – Part 2**.

---

## Learning Objectives

By the end of this project, you should be able to explain, without external help:

- How to write an **asynchronous generator**
- How to use **async comprehensions**
- How to **type-annotate** asynchronous generators
- How Python handles concurrent async tasks
- Why async comprehensions are more efficient than classical loops in async context

---

## Requirements

### General

- Allowed editors: **vi**, **vim**, **emacs**
- All files will be run on Ubuntu **20.04 LTS**, Python **3.9**
- All Python files must:
  - end with a newline
  - start with exactly: `#!/usr/bin/env python3`
  - be executable
  - follow **pycodestyle 2.5.x**
- File length will be checked using `wc`
- A `README.md` at the root is **mandatory**
- All modules must have documentation:
  - `python3 -c 'print(__import__("my_module").__doc__)'`
- All functions and coroutines must have full documentation
  - not just a word — a full sentence describing the purpose
- **Every function must be type-annotated**

---

## Resources

Read or watch:

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-can-i-type-hint-a-generator-in-python-3)


---

## Tasks Summary

| # | Task Name                                      | Description                                                                           | File(s)                        |
|---|------------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------|
| 0 | Async Generator                                | Write `async_generator` yielding 10 random numbers (1 second delay each)             | `0-async_generator.py`         |
| 1 | Async Comprehensions                           | Write `async_comprehension` collecting 10 values from `async_generator`              | `1-async_comprehension.py`     |
| 2 | Runtime of parallel comprehensions             | Write `measure_runtime` to run 4 async comprehensions in parallel and measure time   | `2-measure_runtime.py`         |

---
