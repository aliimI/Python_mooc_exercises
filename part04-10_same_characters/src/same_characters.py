def same_chars(str, index1, index2):
    # i = 1
    # while i <= len(str):
    #     if str[index1] == str[index2]:
    #         return True
    #     return False
    
    if index1 >= len(str) or index2 >= len(str):
        return False
    return str[index1] == str[index2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 1, 3))
