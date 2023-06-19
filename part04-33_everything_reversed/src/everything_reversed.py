# Write your solution here
def everything_reversed(list: list):
    new_list = []
    for i in list:
        new_list.append(i[::-1])
    return new_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
