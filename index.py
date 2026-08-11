# Lesson 1 — Python for a JavaScript Developer

# 1. Variables

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
