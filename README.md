# In-Memory Key-Value Database with Transaction Support

## Overview
This project implements an in-memory key-value database in Python that supports basic transactions. It allows you to perform atomic operations that can be committed or rolled back to maintain data integrity.

## Instructions How to Run the Code

### Prerequisites
Python 3.x installed on your machine.

### Run the Script

- Open a terminal or command prompt.
- Navigate to the directory containing `in_memory_db.py`.
- Run the script using the command: `python in_memory_db.py`

## How to Use

**Initialize the Database:**

```python
db = InMemoryDB()
```


**Begin a Transaction:**

```python
db.begin_transaction()
```

**Put a Key-Value Pair:****

```python
db.put("key", value)
```

**Get a Value by Key:**
```python
value = db.get("key")
```

**Commit the Transaction:**

```python
db.commit()
```

**Rollback the Transaction:**
```python
db.rollback()
```

## Assignment Improvement Suggestions
To improve this assignment, I believe it would be helpful to clarify the expected exception messages for consistency. Including unit tests would enhance code reliability and make grading more straightforward. Providing code style guidelines (PEP 8 compliance) would ensure consistency and readability.