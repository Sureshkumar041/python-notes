print("Closure")


def outer():
    a = 1

    def inner():
        print("a: ", a)

    return inner


result = outer()

# You'll see Python's internal closure information.
print("res: ", result.__closure__)

# Multiple closures can remember different values

print("\nMultiple closures can remember different values")


def team(name: str):
    def player():
        print("Player Name: ", name)

    return player


player_1 = team("Suresh")
player_2 = team("Kevin")

player_1()
player_2()

# Closures + decorators

print("\nClosures + decorators")
