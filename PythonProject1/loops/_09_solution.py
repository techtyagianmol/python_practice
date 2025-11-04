items = input("Enter some items separated by space: ").split()

unique_items = set()
duplicate_items = set()

for item in items:
    if item in unique_items:
        duplicate_items.add(item)
    else:
        unique_items.add(item)

print("Unique items are:", unique_items)
print("Duplicate items are:", duplicate_items)
