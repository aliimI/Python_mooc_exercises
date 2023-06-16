# Write your solution here
def length_of_longest(my_list: list):
    first = len(my_list[0])
    for item in my_list:
        if len(item) >= first:
            first = len(item)
    return first
    
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
    