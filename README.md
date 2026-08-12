Python 🐍

Naal - 11-08-2025 🗓

# Lesson 1 — Python for a JavaScript Developer

1. Variables
2. Strings
3. Lists ≈ JavaScript Arrays
4. Dictionaries ≈ JavaScript Objects
5. if statements
6. for loops
    1. range
7. List Comprehensions
    1. map
    2. filter

# Lesson 2: Functions

1. Functions
2. Default parameters

# Lesson 3 — *args and **kwargs

1. *args
2. **kwargs
3. *agrs and **kwargs

# Lesson 4 — Python * and ** unpacking

1. Python's version of object spread
2. Dictionary merging

Naal - 12-08-2025 🗓

# Lesson 5 — Classes: Python vs JavaScript

1. Classes
2. Add behavior

# Lesson 6 — @classmethod vs @staticmethod

1. Instance method

An instance method is a function defined inside a class that operates directly on an instance (object) of that class.

2. @classmethod

@classmethod in Python is a built-in decorator used to define a method that is bound to the class itself rather than a specific object instance. It automatically receives the class as its first implicit argument, which is conventionally named cls.

3. @staticmethod

@staticmethod is a built-in decorator used to define a method inside a class that does not access or modify the class state or instance state.


```text
instance method
    ↓
needs this/self

classmethod
    ↓
works with the class itself

staticmethod
    ↓
doesn't need object or class state
```
Added class with class & static method.

# Lesson 7 — Inheritance

Inheritance is a core concept in Object-Oriented Programming (OOP) that allows a child class (derived/subclass) to absorb all methods and properties from a parent class (base/superclass).

# Lesson 8 — @dataclass

A Python dataclass is a regular class decorated with @dataclass that automatically generates repetitive special boilerplate methods like __init__(), __repr__(), and __eq__() based on declared type hints.

1. Mutable defaults
2. UserModelCSM into a dataclass

#### 🚀 Now we're getting close to backend Python

```
Python fundamentals
       ↓
Functions
       ↓
Type hints
       ↓
*args / **kwargs
       ↓
Dictionary unpacking
       ↓
Classes
       ↓
Inheritance
       ↓
super()
       ↓
Method overriding
       ↓
classmethod / staticmethod
       ↓
@dataclass  ← CURRENTLY WE'RE HERE 👬
       ↓
Pydantic
       ↓
FastAPI
       ↓
REST API
       ↓
PostgreSQL
       ↓
Authentication
```
