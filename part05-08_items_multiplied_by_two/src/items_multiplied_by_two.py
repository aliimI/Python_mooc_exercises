# Write your solution here
def double_items(my_list: list):
    doubled_list = []
    for item in my_list:
        doubled_list.append(item * 2)
    return doubled_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)