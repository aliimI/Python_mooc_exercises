# Write your solution here
def all_the_longest(my_list: list):
    new_list =[]
    first = 0
    for i in my_list:
        if len(i) >= first:
            first = len(i)

    for i in my_list:
        if len(i) == first:
            new_list.append(i)

            
    return new_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) 