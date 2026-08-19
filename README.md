#    Python 🐍

> Naal - 11-08-2025 🗓

## Lesson 1 — Python for a JavaScript Developer

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

## Lesson 2: Functions

1. Functions
2. Default parameters

## Lesson 3 — *args and **kwargs

1. *args
2. **kwargs
3. *agrs and **kwargs

## Lesson 4 — Python * and ** unpacking

1. Python's version of object spread
2. Dictionary merging

> Naal - 12-08-2025 🗓

## Lesson 5 — Classes: Python vs JavaScript

1. Classes
2. Add behavior

## Lesson 6 — @classmethod vs @staticmethod

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

## Lesson 7 — Inheritance

Inheritance is a core concept in Object-Oriented Programming (OOP) that allows a child class (derived/subclass) to absorb all methods and properties from a parent class (base/superclass).

## Lesson 8 — @dataclass

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
## Lesson 9 — Pydantic.

- TypeScript-style type definitions
- Request validation
- Data parsing/serialization

1. Your dataclass
    Python doesn't automatically validate incoming values.

2. Pydantic Model

```bash
pip install pydantic
```

    - Step 1 — Your first Pydantic model
    - Step 2 — Try Pydantic's parsing 


```text
Python type hint
    ↓
Tells developers/tools what type is expected

Pydantic
    ↓
Actually validates/parses the data at runtime
```
3. Nested Models

> Naal - 13-08-2025 🗓

#### 🎯 Final part of Lesson 9: Field Validation

## Lesson 10 — FastAPI

First, install FastAPI + Uvicorn

```bash
python -m pip install fastapi uvicorn
```
1. Create your first API
2. Start the server

From your project directory:

```bash
python -m uvicorn file-name:app --reload
```

3. The cool part 😎

FastAPI automatically gives you API documentation.

Open:

```bash
http://127.0.0.1:8000/docs
```

You'll see Swagger UI.

And:

```bash
http://127.0.0.1:8000/redoc
```

gives you ReDoc.
So unlike Express, you get interactive API documentation with very little extra work.

#### Get API

1. with path parameteres
2. Query parameters

#### Post API

You learned Pydantic separately:

```text
BaseModel
Field
Validation
Nested Models
model_dump()
```
And now you're using it inside FastAPI:

```text
POST request
     ↓
Pydantic Model
     ↓
Validation
     ↓
Python function
     ↓
JSON response
```
#### Response Models

⭐ Important concept

This is exactly why we use separate request/response models:

```text
Client
  │
  │ password included
  ↓
PlayerBM
  │
  │ validated
  ↓
Your service
  │
  ↓
CreatePlayerRes
  │
  │ password excluded
  ↓
Client
```

That's real API design.

#### HTTP status codes


✅ Lesson 10 progress

 - FastAPI app & routes ✅
 - GET endpoints ✅
 - Path parameters ✅
 - Query parameters ✅
 - POST request body ✅
 - Pydantic + FastAPI ✅
 - Request models ✅
 - Response models ✅
 - Sensitive field exclusion (password) ✅
 - HTTP status codes ✅

 #### CRUD: GET /players

Step 1 — Create our fake database
Step 2 — Create GET endpoint
Step 3 — Create post endpoint
Step 4 — PUT /players/{id}
Step 5 — DELETE. 😎🔥

```text
FastAPI
   +
Pydantic
   +
Path parameters
   +
Query parameters
   +
Request validation
   +
Response models
   +
HTTP status codes
   +
HTTPException
   +
CRUD operations
```
## Lesson 11 — FastAPI Dependency Injection

1. 🎯 Dependency + Query Parameter
2. 🏏 Next ball: Reusable dependencies
3. 🏏 Next level: Dependency with a class


🏆 Lesson 11 — Dependency Injection COMPLETE

You've covered:

- Depends() ✅
- Simple dependencies ✅
- Dependencies with query parameters ✅
- Reusing dependencies across routes ✅
- Typed dependencies ✅
- Class-based dependencies ✅
- __call__() with FastAPI dependencies ✅

## Lesson 12 — SQLAlchemy + PostgreSQL

Think MERN:

```text
Express     → FastAPI
Mongoose    → SQLAlchemy
MongoDB     → PostgreSQL
```

1. — Install SQLAlchemy + PostgreSQL driver

Inside your activated .venv:

```bash
python -m pip install sqlalchemy psycopg2-binary
```

2.  — Create the database connection

3.  — Create the User Model

> Naal - 14-08-2025 🗓

4.  — User Pydantic Schema

API flow CLIENT - SERVER

```text
Client
  ↓
UserCreate
  ↓
Service
  ↓
SQLAlchemy User
  ↓
PostgreSQL
  ↓
SQLAlchemy User
  ↓
UserResponse
  ↓
Client
```

#### DB Session

database.py - Has three responsibilities:

```text
database.py
│
├── engine              → connects to PostgreSQL
├── SessionLocal        → creates DB sessions
└── get_db()            → gives session to FastAPI and closes it
```

5. User Service

6. User Route


### Connect Router to main.py

User APIs

1. Create User
2. Get All User
3. Get User Profile
4. Update User — PUT /users/{user_id}
5. Update User - Put /users/update-user-status

## Lesson 13 - File Upload

```text
1. Upload one file
        ↓
2. Read file metadata
        ↓
3. Save file to disk
        ↓
4. Generate unique filename
        ↓
5. Store file details in PostgreSQL
        ↓
6. Return file response
        ↓
7. Download file
        ↓
8. Delete file / soft delete
```

#### 1. First concept: UploadFile

```text
Browser
   ↓
UploadFile
   ↓
FastAPI
   ↓
return metadata
```

> Naal - 17-08-2025 🗓

#### Save the physical file

```text
Browser
   ↓
UploadFile
   ↓
Generate unique filename
   ↓
Save file to disk
   ↓
Create File DB record
```
1. Create the directory
2. Update the upload endpoint

#### Save File details to PostgreSQL

#### user_id and file_category proper API inputs.

## Flow we'll build

```test
                    ┌──────────────┐
                    │  POST /users │
                    └──────┬───────┘
                           ↓
                     Create User
                           │
                           │
                    ┌──────▼───────┐
                    │ POST /login  │
                    └──────┬───────┘
                           ↓
                  Verify credentials
                           ↓
                    Generate JWT
                           ↓
                 access_token + type
                           ↓
              Authorization: Bearer ...
                           ↓
                get_current_user()
                           ↓
                    current_user.id
```

We'll add these pieces one by one:

1. Password hashing
2. Login schema
3. JWT generation
4. Login API
5. JWT verification
6. get_current_user dependency
7. Protect File API

> Naal - 18-08-2025 🗓

#### JWT

1. JWT generation

```bash
pip install PyJWT
```
Implemented the JWT token in login API

HTTPBearer() tells FastAPI:

This dependency requires an Authorization: Bearer <token> header.

So the dependency chain is:

```text
GET /users/me
       │
       ↓
Depends(get_current_user)
       │
       ↓
Depends(security)
       │
       ↓
HTTPBearer()
       │
       ↓
Authorization: Bearer <JWT>
       │
       ↓
JWT decoded
       │
       ↓
User fetched from DB
       │
       ↓
current_user
       │
       ↓
Your API function runs
```
#### File retrieval

APIs :-

Get all files for the logged-in user

Get file by Id

##### Download / serve the physical file

Flow
```text
JWT
 ↓
current_user
 ↓
File ID + current_user.id
 ↓
Database ownership check
 ↓
Get physical path
 ↓
Check file exists
 ↓
FileResponse
 ↓
Browser receives actual file
```
> Naal - 19-08-2025 🗓

#### File soft delete

## SQLAlchemy relationships

1. ForeignKey vs relationship()

```python
user_id: Mapped[int] = mapped_column(
    ForeignKey("users.id")
)
```

Now PostgreSQL understands:

```text
files.user_id
      ↓
users.id
```
That's a database relationship.

2. Then what is relationship()?

relationship() is an ORM-level relationship.

```text
User
 ├── profile_image → File
 └── files[]       → File[]
```

one-to-one
one-to-many

## Lesson 14 — Python Enum

Python's Enum lets us define a fixed set of allowed values.

1. What's the problem with plain str?
2. What is an Enum?

An Enum is a type containing a fixed collection of named values.

3. Why str, Enum?

```python
class FileStatus(str, Enum):
```

4. Enum has two important things

```python
class FileStatus(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"
```

- Name
```python
FileStatus.ACTIVE.name

# ACTIVE
```

- Value
```python
FileStatus.ACTIVE.value

# active
```

ACTIVE --> The uppercase part is the Python identifier.

active --> The lowercase part is the actual value.

5. Let's apply it to real model

Instead of:
```python
status: Mapped[str]
```

Follow this:
```python
status: Mapped[FileStatus]
```

6. Why is this better?

Enum
```python
FileStatus.ACTIVE
FileStatus.DELETED
FileStatus.ARCHIVED
FileStatus.PROCESSING
FileStatus.FAILED
```
And if someone tries:

```python
FileStatus.SOMETHING
```
    - Python immediately tells you it doesn't exist.

7. Implementation



### Project folder structure

```text
Python/
├── .venv/
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── player.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── player_service.py
│   │
│   └── routes/
│       ├── __init__.py
│       └── player.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```