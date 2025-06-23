name = input("Please insert you name: ")

age = int(input("Please enter your age: "))

height = float(input("Please enter your height in meters: "))

is_student = input("Are you a student? (Yes/No): ").lower() == "yes"    # (YES, Yes, yES, yes)
print(type(is_student))

print(f"Hello {name}!")

if is_student:
  print("You are a student")
else:
  print("You are not a student")

print("Your age is {} and your height is {:.2f} metes".format(age, height))