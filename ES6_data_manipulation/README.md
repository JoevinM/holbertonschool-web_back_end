# 📘 ES6 Data Manipulation – Foundations v2.1 (Part 3)

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Tasks Summary](#tasks-summary)

---

## Project Overview

This project focuses on **data manipulation in JavaScript using ES6 features**.
You will work with arrays, objects, and modern data structures such as **Set**, **Map**, **WeakMap**, and **Typed Arrays**.

The goal is to strengthen your understanding of functional programming concepts and modern JavaScript patterns commonly used in real-world applications.

This project is part of **Foundations v2.1 – Part 3**.

---

## Learning Objectives

By the end of this project, you should be able to explain, without external help:

### General
- How to use `map`, `filter`, and `reduce` on arrays
- How to work with **Typed Arrays**
- How to use the **Set**, **Map**, and **WeakMap** data structures
- How to combine multiple array operations efficiently
- How to manipulate structured data in a clean and readable way using ES6

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
- All tests and lint checks must pass:
  ```bash
  npm run full-test

---

## Resources

Read or watch:

[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
[Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Typed_arrays)
[Set Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
[Map Data Structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
[WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

---

## Tasks Summary

| #  | Task Name               | Description                                      | File                        |
| -- | ----------------------- | ------------------------------------------------ | --------------------------- |
| 0  | Basic list of objects   | Create an array of student objects               | `0-get_list_students.js`    |
| 1  | More mapping            | Extract student IDs using `map`                  | `1-get_list_student_ids.js` |
| 2  | Filter                  | Filter students by location                      | `2-get_students_by_loc.js`  |
| 3  | Reduce                  | Sum student IDs using `reduce`                   | `3-get_ids_sum.js`          |
| 4  | Combine                 | Update student grades using `filter` and `map`   | `4-update_grade_by_city.js` |
| 5  | Typed Arrays            | Create and manipulate an `Int8Array`             | `5-typed_arrays.js`         |
| 6  | Set data structure      | Convert an array into a `Set`                    | `6-set.js`                  |
| 7  | More set data structure | Check values existence between `Set` and `Array` | `7-has_array_values.js`     |
| 8  | Clean set               | Build a formatted string from a `Set`            | `8-clean_set.js`            |
| 9  | Map data structure      | Create a groceries `Map`                         | `9-groceries_list.js`       |
| 10 | More map data structure | Update unique items in a `Map`                   | `10-update_uniq_items.js`   |

---
