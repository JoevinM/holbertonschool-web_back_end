# Python – Variable Annotations

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Table of Tasks](#table-of-tasks)

---

## Project Overview

This project introduces advanced Python typing: type annotations, complex type hints, callables, tuples, unions, and static type checking with mypy.
You will improve code readability, enforce contracts, and understand how typing integrates into real-world Python development.

This is part of Foundations v2.1 — Part 2 and contributes to your backend engineering fundamentals.

---

## Learning Objectives
By the end of this project, you should be able to explain to anyone, without the help of Google:

-Type annotations in Python 3
-How to specify function signatures and variable types
-The concept of duck typing
-How to validate code using mypy
-The role of annotations in modern Python codebases
-How to annotate complex types (List, Tuple, Union, Callable, Iterable)

---

## Requirements

### General

-Allowed editors: vi, vim, emacs
-All files will be interpreted on Ubuntu 20.04 LTS, Python 3.9
-All files must:

-end with a new line
-start with exactly: #!/usr/bin/env python3
-be executable
-A README.md file is mandatory at the root
-Code must follow pycodestyle 2.5
-File length will be checked using wc
-All modules must have documentation
-All classes must have documentation
-All functions must have documentation (inside and outside classes)
-Documentation must be a sentence explaining the purpose, not one word
-You must use Python type annotations everywhere

---

## Resources

Read or watch:
- [Python 3 Typing Documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

---

## Table of Tasks

| # | Task name                      | Description                                                             | File(s)                 |
| - | ------------------------------ | ----------------------------------------------------------------------- | ----------------------- |
| 0 | Basic annotations — add        | Create `add(a: float, b: float) -> float` returning the sum             | `0-add.py`              |
| 1 | Basic annotations — concat     | Create `concat(str1: str, str2: str) -> str` concatenating two strings  | `1-concat.py`           |
| 2 | Basic annotations — floor      | Create `floor(n: float) -> int` returning `math.floor(n)`               | `2-floor.py`            |
| 3 | Basic annotations — to string  | Create `to_str(n: float) -> str` converting float to string             | `3-to_str.py`           |
| 4 | Define variables               | Annotate and define: `a`, `pi`, `i_understand_annotations`, `school`    | `4-define_variables.py` |
| 5 | Complex types — list of floats | Create `sum_list(input_list: List[float]) -> float`                     | `5-sum_list.py`         |
| 6 | Complex types — mixed list     | Create `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`      | `6-sum_mixed_list.py`   |
| 7 | Complex types — tuple output   | Create `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`       | `7-to_kv.py`            |
| 8 | Complex types — functions      | Create `make_multiplier(multiplier: float) -> Callable[[float], float]` | `8-make_multiplier.py`  |
| 9 | Duck typing — annotate         | Annotate `element_length(lst)` with `Iterable[Sequence]`                | `9-element_length.py`   |

---

