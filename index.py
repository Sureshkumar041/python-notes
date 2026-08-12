# Lesson 1 — Python for a JavaScript Developer

# 1. Variables

from dataclasses import dataclass, field
from typing import TypedDict

print("1. Variable 🥏")

name = "string value"
count = 10
is_human = True

print(type(name))
print(type(count))
print(type(is_human))

# 2. Strings

print("\n2. Strings 🥏")

first_name = "suresh"
last_name = "kumar"

print(f"{first_name} {last_name}")

# 3. Lists ≈ JavaScript Arrays

print("\n3. Lists ≈ JavaScript Arrays 🥏")

users = ["sk", "ak", "k"]

print(users[0])
print(users[-1])

# 4. Dictionaries ≈ JavaScript Objects

print("\n4. Dictionaries ≈ JavaScript Objects")

user = {"name": "suresh", "age": 25, "role": "developer"}

print(user)
print(user["name"])
print(user.get("favorite"))

# 5. if statements

print("\n5. if statements")

if user["age"] >= 18:
    print(f"{user['name']} is eligible")
else:
    print(f"{user['name']} is not eligible")

# 6. for loops

print("\n6. for loops")

for user_name in users:
    print(user_name)

# range()

print("\n6.1 range()")

for index in range(len(users)):
    print(index)

# 7. List Comprehensions

print("\n7. List Comprehensions")

print("\n7.1 map")

persons1 = [{"name": u} for u in users]

print(persons1)

print("\n7.2 filter")

persons2 = [u for u in users if u == "sk"]

print(persons2)

# First exercise

print("\nFirst exercise")

users_input = [
    {"name": "John", "age": 25, "active": True},
    {"name": "Jane", "age": 17, "active": True},
    {"name": "Mike", "age": 30, "active": False},
    {"name": "Sarah", "age": 22, "active": True},
]

# produces a list containing the names of users who are:

# active
# 18 or older

print([u["name"] for u in users_input if u["active"] and u["age"] >= 18])

# Lesson 2: Functions

print("\nFunctions")


def add(a, b):
    return a + b


add_result = add(1, 2)

print(add_result)

print("\nDefault parameters")


def default_parameters_func(a=1, b=2) -> int:
    return a - b


default_parameters_func_result = default_parameters_func()

print(default_parameters_func_result)

# 🚀 Your next challenge

# get_active_users(users)
# that returns the names of users who are active.

print("\nget_active_users(users)")


def get_active_users(users: list[dict]) -> list[str]:
    return [u["name"] for u in users if u["active"]]


get_active_users_result = get_active_users(users_input)

print(get_active_users_result)

# Lesson 3 — *args and **kwargs

print("\n*args")

# 1. *args
# Allows a function to receive any number of positional arguments.


def add_nums(*nums):
    return sum(nums)


print(add_nums(1, 2))

# 2. **kwargs
# This captures arbitrary keyword arguments.

print("\n**kwargs")


def create_user(**kwargs):
    print(kwargs)


create_user(name="Suresh", age=25, role="developer")

# kwargs is a dictionary.

print("\n*agrs and **kwargs")


def test(required, *args, **kwargs):
    print(required)
    print(args)
    print(kwargs)


test("Hey man", 10, 20, name="Suresh", age=25)

# 🧠 Your challenge

# Imagine you're building a reusable API helper.

# Create:

# def create_user(name, **details):
#     ...

# This should work:

# user = create_user(
#     "John",
#     age=25,
#     role="developer",
#     active=True
# )

# Expected result:

# {
#     "name": "John",
#     "age": 25,
#     "role": "developer",
#     "active": True
# }

print("\ncreate_user(name, **details)")


def create_user_service(name: str, **details: object) -> dict:
    return {"name": name, **details}


user_dict = create_user_service("suresh", age=25, role="developer", active=True)

print(user_dict)

# Lesson 4 — Python * and ** unpacking

# That's basically Python's version of object spread:

# return {"name": name, **details}

# Dictionary merging

print("\nDictionary merging")

user = {"name": "suresh", "age": 25}
extra_field = {"role": "developer"}

merging_dict = {**user, **extra_field}

print(merging_dict)

# 🚀 Your challenge
# Write a function:

# def update_user(user, **updates):
#     ...

# Given:

# user = {
#     "name": "Suresh",
#     "age": 25,
#     "role": "developer",
#     "active": True
# }

# Calling:

# updated = update_user(
#     user,
#     age=26,
#     role="senior developer"
# )

# should produce:

# {
#     "name": "Suresh",
#     "age": 26,
#     "role": "senior developer",
#     "active": True
# }

# Try to solve it using ** unpacking rather than modifying the original dictionary.

print("\nupdate_user_service")


def update_user_service(
    user: dict[str, object], **updates: object
) -> dict[str, object]:
    return {**user, **updates}


user_input_1 = {"name": "Suresh", "age": 25, "role": "developer", "active": True}

updated_user = update_user_service(user_input_1, age=26, role="senior developer")

print(updated_user)

# Lesson 5 — Classes: Python vs JavaScript

print("\nClasses")


# Your challenge

# Create a User class with:

# name
# email
# age
# is_active

# And a method:

# get_profile()

# that returns:

# {
#     "name": "Suresh",
#     "email": "suresh@example.com",
#     "age": 25,
#     "is_active": True
# }


class User(TypedDict):
    name: str
    age: int
    email: str
    is_active: bool


class UserModel:
    def __init__(self, name: str, email: str, age: int, is_active: bool):
        self.name = name
        self.email = email
        self.age = age
        self.is_active = is_active

    def get_profile(self) -> User:
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "is_active": self.is_active,
        }

    def is_adult(self) -> bool:
        return self.age >= 18

    def deactivate(self) -> None:
        self.is_active = False


user_cl = UserModel("suresh", "sureshkumar@maildrop.cc", 25, True)

print(user_cl.get_profile())

# 🚀 Next challenge: Add behavior

# Right now your class stores data and returns it.

# Let's make it behave more like a real backend domain object.

# Add these methods:

# is_adult()

# Returns True if age >= 18.

# And:

# deactivate()

# Changes:

# is_active = False

# So this should work:

# user = UserModel(
#     "suresh",
#     "sureshkumar@maildrop.cc",
#     25,
#     True
# )

# print(user.is_adult())   # True

# user.deactivate()

# print(user.get_profile())

# Expected:

# True

# {
#     "name": "suresh",
#     "email": "sureshkumar@maildrop.cc",
#     "age": 25,
#     "is_active": False
# }

print("\nAdd behavior")

print(user_cl.is_adult())
user_cl.deactivate()
print(user_cl.get_profile())

# Lesson 6 — @classmethod vs @staticmethod

# 1. Instance method

print("\n1. Instance method")

# def is_adult(self) -> bool:
#     return self.age >= 18

# user.is_adult()

# 2. @classmethod

print("\n2. @classmethod")

# A class method receives cls instead of self.


class UserModalCM:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_guest(cls):
        return cls("Suresh", 24)

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])


user_modal_cm = UserModalCM.create_guest()

print(f"Create Guest - Name: {user_modal_cm.name}")

user_modal_cm1 = UserModalCM.from_dict({"name": "Sk", "age": 20})

print(f"From dict - Name: {user_modal_cm1.name}")

# 3. @staticmethod

print("\n3. @staticmethod")

# A static method doesn't need self or cls.


class UserModalSM:
    def is_valid_age(age: int) -> bool:
        return age >= 18


print(UserModalSM.is_valid_age(18))
print(UserModalSM.is_valid_age(17))

# Your challenge 🚀

"""
Add these two methods to your UserModel:

@classmethod
def create_guest(cls):
    ...

It should create:

UserModel("Guest", "guest@example.com", 18, True)

And:

@staticmethod
def is_valid_age(age: int) -> bool:
    ...

It should return True when age is between 18 and 100, otherwise False.

Then test:

guest = UserModel.create_guest()

print(guest.get_profile())
print(UserModel.is_valid_age(25))
print(UserModel.is_valid_age(150))
"""
print("\nAdd class & static methods in Classes")


class UserModelCSM:
    def __init__(self, name, email, age, is_active):
        self.name = name
        self.email = email
        self.age = age
        self.is_active = is_active

    def get_profile(self) -> User:
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "is_active": self.is_active,
        }

    @classmethod
    def create_guest(cls):
        return cls("Kevin", "kevin@maildrop.cc", 33, True)

    @staticmethod
    def is_valid_age(age: int) -> bool:
        return 18 <= age <= 100

    # chained comparisons


user_modal_csm = UserModelCSM.create_guest()

user_modal_csm_val = user_modal_csm.get_profile()

print(user_modal_csm_val)
print(user_modal_csm.is_valid_age(25))
print(user_modal_csm.is_valid_age(150))

# Lesson 7 — Inheritance

print("\n7 — Inheritance")


class AdminModel(UserModelCSM):
    def __init__(self, name, email, age):
        super().__init__(name, email, age, True)
        self.role = "admin"

    def delete_user(self, user: UserModelCSM) -> None:
        print(f"{self.name} deleted {user.name}")

    def get_profile(self) -> User:
        profile = super().get_profile()
        profile["role"] = self.role
        return profile


admin_model = AdminModel("Liya", "liya@maildrop.cc", 30)


print(admin_model.get_profile())
admin_model.delete_user(user_modal_csm)
print(admin_model.get_profile())

# Lesson 8 — @dataclass.

print("\n8 — @dataclass")


@dataclass
class UserDC:
    name: str
    email: str
    age: int
    is_active: bool = True

    def deactivate(self) -> None:
        self.is_active = False

    def is_valid_age(self) -> bool:
        return self.age >= 18


user_dc = UserDC("Sandy", "sandy@maildrop.cc", 35)

print(user_dc)

user_dc.deactivate()

print(user_dc.is_valid_age())

print(user_dc)

# ⚠️ Important: Mutable defaults

print("\n⚠️ Important: Mutable defaults")


@dataclass
class UserDCList:
    name: str
    visited_place: list[str] = field(default_factory=list)
    # default_factory=list creates a new list for every instance.


user_dc_list1 = UserDCList("Suresh")
user_dc_list2 = UserDCList("Kevin")

user_dc_list1.visited_place.append("Chennai")

print(f"user_dc_list1 - {user_dc_list1}")
print(f"user_dc_list2 - {user_dc_list2}")

# 🎯 Your challenge

print("\nUserModelCSM into a dataclass")

"""
Convert your previous UserModelCSM into a dataclass.

Requirements:

name: str
email: str
age: int
is_active: bool = True

Add:

is_adult() -> bool
deactivate() -> None

And add a class method:

create_guest()

that creates:

name = "Guest"
email = "guest@example.com"
age = 18
is_active = True
"""


@dataclass
class UserModelCMWithDC:
    name: str
    email: str
    age: int
    is_active: bool = True

    @classmethod
    def create_guest(cls):
        return cls("Jack", "jack@maildrop.cc", 34)

    def deactivate(self) -> None:
        self.is_active = False

    def is_valid_age(self) -> bool:
        return self.age >= 18


user_modal_csm_dc = UserModelCMWithDC.create_guest()

print(user_modal_csm_dc)

user_modal_csm_dc.deactivate()

print(user_modal_csm_dc.is_valid_age())

print(user_modal_csm_dc)
