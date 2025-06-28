# populate dict
products = {
    1:"apple",
    2:"banana",
    3:"honey",
    4:"melon"
}
print(f"Initial dict: {products}")

# insert/update a new key: value pair
products[3] = "orange"
print(f"Dict after insertion: {products}")

# read an element (access)
# product_1 = products[1]
# print(product_1)

# product_10 = products[10]
# print(product_10)

product_10 = products.get(10, "Out of stock")
print(product_10)

del products[1]
print(f"After deleting key 1 {products}")

removed_item = products.pop(10, "Item not found")
print(f"Removed item: {removed_item}")
print(f"After remove function: {products}")

# Delete: remove the 'last' inserted item with popitem()
key, value = products.popitem()
print(f"Key:{key}, Value:{value}")

print(products)

key_to_check = 2

if key_to_check in products:
    print(f"Key: {key_to_check} exists")
else:
    print(f"Key: {key_to_check} does not exist")

# iterate
for key in products:
    print(key, ":", products[key])

print("-----------")
for key in products.keys():
    print(key, ":", products[key])

print("-----------")
for value in products.values():
    print(value)

print("-----------")
for key, value in products.items():
    print(f"Key: {key}, Value: {value}")