# Write your solution here
def list_sum(list1, list2: list):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])
    return new_list
    

if __name__ == "__main__":
    my_list1 = [1, 2, 3, 6]
    my_list2 = [7, 8, 9, 3]
    result = list_sum(my_list1, my_list2)
    print(result)
    
