# 📘 Python – Pagination

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Tasks Summary](#tasks-summary)

---

## Project Overview

This project introduces techniques for **REST API pagination**, including:

- Basic pagination using `page` and `page_size`
- Hypermedia pagination (HATEOAS metadata)
- Deletion-resilient pagination using indexed datasets

These concepts are essential for handling large datasets efficiently and safely.

This project is part of **Foundations v2.1 – Part 3**.

---

## Learning Objectives

By the end of this project, you should be able to explain:

- How to paginate datasets using `page` and `page_size`
- How to implement hypermedia pagination metadata
- How to make pagination **resilient to deletions**
- How backend services handle large datasets in paginated form
- Why pagination is critical for REST API design

---

## Requirements

### General

- All files interpreted with **Python 3.9** on **Ubuntu 20.04 LTS**

- All Python scripts must:
  - end with a newline
  - start with exactly: `#!/usr/bin/env python3`
  - be executable
  - follow **pycodestyle 2.5.x**
- A `README.md` is **mandatory**

- File length will be tested with `wc`

- All modules must contain full documentation
  Example:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'

- All functions must contain full documentation:

```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```
- Documentation must be a full, clear sentence

- All functions must be type-annotated

- Use the dataset: Popular_Baby_Names.csv

## Resources

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)


## Tasks Summary

| # | Task Name                                | Description                                        | File(s)                          |
| - | ---------------------------------------- | -------------------------------------------------- | -------------------------------- |
| 0 | Simple helper function                   | Write `index_range` returning start/end indexes    | `0-simple_helper_function.py`    |
| 1 | Simple pagination                        | Build `Server.get_page()` for basic pagination     | `1-simple_pagination.py`         |
| 2 | Hypermedia pagination                    | Implement `get_hyper()` returning metadata         | `2-hypermedia_pagination.py`     |
| 3 | Deletion-resilient hypermedia pagination | Build `get_hyper_index()` using an indexed dataset | `3-hypermedia_del_pagination.py` |
