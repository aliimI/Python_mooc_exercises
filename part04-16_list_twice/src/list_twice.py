# Write your solution here
orig_list = []
while True:
    item = int(input("New item:"))
    if item == 0:
        print("Bye!")
        break
    orig_list.append(item)
    print(f"The list now: {orig_list}")
    print(f"The list in order: {sorted(orig_list)}")
