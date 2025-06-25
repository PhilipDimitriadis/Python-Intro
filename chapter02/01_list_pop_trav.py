ages = [19, 23, 34, 55]

print("Initial list of ages:", ages)

for age in ages:
  print(age, end=", ")
print()

#Challenge
print("Initial list of ages: [", end="")
for i, age in enumerate(ages):
    print(age, end="")
    if i < len(ages) - 1:
        print(", ", end="")
print("]")
  

for index, value in enumerate(ages):
  print(f"Index: {index}, Value: {value}")