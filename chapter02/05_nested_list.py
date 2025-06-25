items = [1, 2, 3.14, True, "Hello CF7 friends"]

for item in items:
    print(item, end=", ")
print()

nested_list = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# nest_list = [[1,2], [3, 4], [5, 6]]

print(f"first list item: {nested_list[0]}")

# Print '3'
print(nested_list[1][0])

# [3, 4], [1, 2]
print(f"{nested_list[1]}, {nested_list[0]}")

#Challenge, slicing
print(nested_list[-2::-1])

