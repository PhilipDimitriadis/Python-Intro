# range(10)

a = range(10)
print(f"Type of a: {type(a)}")

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print()
print("-" * 10)

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
else:
    print("Loop ended normally")
print()

# List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes", "Peaches", "Watermelon"]

fruit_to_check = "Melon"

for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list")
        break
else:
    print(f"{fruit_to_check} not in the list")

# Happy hour 
print("Why do Python devs never get lost")
print("Because they always know where 'in' in!")

if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in the list")
else:
    print(f"{fruit_to_check} not in the list")

# Challenge
print("One line exe")
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else "not in"} the list")