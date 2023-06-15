# Write your solution here
my_list = []
i = 1
print(f"The list is now {my_list}")
while True:
    
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == "x":
        print("Bye!")
        break
    elif action == "d":
        my_list.append(len(my_list) + 1)
    elif action == "r":
        my_list.pop(len(my_list) - 1)
    i += 1
    print(f"The list is now {my_list}")

