bag = {"eggs", "oranges", "bananas", "eggs"}
print(f"Initial bag: {bag}")

# add a new item
bag.add("grapes")
print("Bag after adding grapes:", bag)

# remove
# bag.remove("bananas")
# print("Bag after removing bananas:", bag)

for item in bag:
    print(item, end=" ")
print()