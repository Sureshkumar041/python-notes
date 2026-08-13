from pydantic import BaseModel, Field

# 2. Pydantic Modes
#  pip install pydantic


class UserBM(BaseModel):
    name: str
    email: str
    age: int
    is_active: bool = True


# Step 1 — Your first Pydantic model
# print("\nfirst Pydantic model")
# user_bm = UserBM(name="suresh", email="suresh@maildrop.cc", age=25)


# Step 2 — Try Pydantic's parsing
print("\nPydantic's parsing")
user_bm = UserBM(name="suresh", email="suresh@maildrop.cc", age="25")

# Step 3 — Try invalid data 💥
# print("\nInvalid data 💥")
# user_bm = UserBM(name="suresh", email="suresh@maildrop.cc", age="Twenty five")
# // error -  Input should be a valid integer, unable to parse string as an integer


print(user_bm)
print(type(user_bm.age))

# 🎯 Next exercise: Nested Models

print("\n🎯 Next exercise: Nested Models")


class AddressBM(BaseModel):
    city: str
    country: str


class UserNestedBM(BaseModel):
    name: str
    email: str
    age: int
    is_active: bool = True
    address: AddressBM


user_nested = {
    "name": "kevin",
    "email": "kevin@maildrop.cc",
    "age": 33,
    "address": {"city": "Trichy", "country": "India"},
}

user_nested_bm = UserNestedBM(**user_nested)

print("user_nested_bm: ", user_nested_bm)
print(user_nested_bm.address.city)
print(user_nested_bm.model_dump())
# converts the whole nested model into normal Python dictionaries.

# 🎯 Final part of Lesson 9: Field Validation

print("\n🎯 Final part of Lesson 9: Field Validation")


class UserBMWithValidation(BaseModel):
    name: str = Field(min_length=3)
    email: str
    age: int = Field(ge=18)
    is_active: bool = True


# will fail validation.
# user_bm_validate = UserBMWithValidation(name="sandy", email="sandy@maildrop.cc", age=15)

user_bm_validate = UserBMWithValidation(name="sandy", email="sandy@maildrop.cc", age=25)

print(user_bm_validate)

print("\nYour challenge 🔥 - Product Data")


class ProductBMWithValidation(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


product_bm_validate = ProductBMWithValidation(
    name="Head Phone", price=10.00, quantity=1
)

print(product_bm_validate)

# Lesson 10 — FastAPI
