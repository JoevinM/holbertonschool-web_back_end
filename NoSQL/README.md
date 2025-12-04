# 📘 NoSQL – Foundations v2.1 · Part 3

## Table of Contents
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Tasks Summary](#tasks-summary)

---

## Project Overview

This project introduces **NoSQL databases**, with a focus on **MongoDB**, a leading document-oriented database.

You will learn to:

- Understand the differences between SQL and NoSQL
- Manipulate MongoDB via shell commands
- Insert, update, delete, and query documents
- Use **PyMongo** to interact with MongoDB in Python
- Write Python functions to perform CRUD operations
- Process and analyze log data stored in MongoDB

This project is part of **Foundations v2.1 – Part 3**.

---

## Learning Objectives

By the end of this project, you should be able to explain, without external help:

### General
- What **NoSQL** means
- Differences between **SQL** and **NoSQL**
- What **ACID** is
- What **document storage** means
- Types of NoSQL databases
- Benefits of NoSQL systems
- How to **query**, **insert**, **update**, and **delete** information in MongoDB
- How to use the **mongo shell**
- How to use **PyMongo** in Python

---

## Requirements

### MongoDB Command Files
- All scripts run on **Ubuntu 20.04 LTS** using **MongoDB 4.4**
- Files must end with a newline
- First line must be a comment: `// my comment`
- A `README.md` at the root is mandatory
- File length will be checked with `wc`

---

### Python Scripts

- All scripts run on **Python 3.9** with **PyMongo 4.8.0**
- Files must end with a newline
- First line must be exactly:
  `#!/usr/bin/env python3`
- Code must follow **pycodestyle 2.5.\***
- A `README.md` is mandatory
- All modules must contain documentation (`__doc__`)
- All functions must contain documentation
- Code must **not** execute on import → use:
  ```python
  if __name__ == "__main__":

---

## Resources

Read or watch:

- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [The mongo Shell](https://www.mongodb.com/docs/mongodb-shell/)


---

| #  | Task                | Description                                               | File                       |
| -- | ------------------- | --------------------------------------------------------- | -------------------------- |
| 0  | List all databases  | Shell script listing all MongoDB databases                | `0-list_databases`         |
| 1  | Create/use database | Switch to or create `my_db`                               | `1-use_or_create_database` |
| 2  | Insert document     | Insert `{ name: "Holberton school" }`                     | `2-insert`                 |
| 3  | All documents       | List all docs in `school` collection                      | `3-all`                    |
| 4  | Matches             | List docs matching `name="Holberton school"`              | `4-match`                  |
| 5  | Count               | Print number of documents in collection                   | `5-count`                  |
| 6  | Update              | Add field `address="972 Mission street"` to matching docs | `6-update`                 |
| 7  | Delete              | Delete documents matching `name="Holberton school"`       | `7-delete`                 |
| 8  | Python: list all    | Python function listing all documents                     | `8-all.py`                 |
| 9  | Python: insert      | Insert document using kwargs                              | `9-insert_school.py`       |
| 10 | Update topics       | Update topics list for a school                           | `10-update_topics.py`      |
| 11 | Schools by topic    | Return schools teaching a given topic                     | `11-schools_by_topic.py`   |
| 12 | Log stats           | Statistics from Nginx logs stored in MongoDB              | `12-log_stats.py`          |
