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