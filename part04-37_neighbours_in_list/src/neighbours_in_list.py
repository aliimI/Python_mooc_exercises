# Write your solution here  
def longest_series_of_neighbours(my_list: list):
    current_length = 1
    longest_length = 1

    for i in range(1, len(my_list)):
        if abs(my_list[i-1]-my_list[i]) == 1:
            current_length += 1
        else:
            current_length = 1

        if current_length > longest_length:
            longest_length = current_length
    return longest_length
    

if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 9, 10]
    print(longest_series_of_neighbours(my_list))
