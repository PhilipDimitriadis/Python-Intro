fruits = ["Apple", "Banana", "Cherry", "Apple"]

print(f"Initial list: {fruits}")

# Add a specific fruit at the end of the list
fruits.append("Berry")
print("After adding Berry: ", fruits)

fruits.extend(["Grapes", "Fig"])
print("After adding Grapes, Fig", fruits)

# Insert an element in a specific position
fruits.insert(1, "Coconut")
print("After adding Coconut", fruits)

# Update the first element
fruits[0] = "Watermelon"
print("After updating the first element: ", fruits)

# Update a slice of list (two elements)
fruits[1:3] = ["A", "B", "C"]
print("After slicing: ", fruits)

# pop()
removed_item = fruits.pop()
print(f"Removed item: {removed_item}")
print("After pop: ", fruits)

# Remove
fruits.remove("C")
print("After removing('C'):", fruits)

#fruits.remove("D")
#print("After removing('D'):", fruits)

idx = fruits.index("A")
print(idx)

item_to_remove = "Grapes"

if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"{item_to_remove} removed")
else:
    print("Insert a fruit tha't on the list")