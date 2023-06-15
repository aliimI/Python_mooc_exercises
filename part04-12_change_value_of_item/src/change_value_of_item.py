# Write your solution here
my_list = [1, 2, 3, 4, 5]
while True:
    index = int(input("Enter index: "))
    if index == -1:
        break
    new_val = int(input("New value: "))

    my_list[index] = new_val 
    print(my_list)