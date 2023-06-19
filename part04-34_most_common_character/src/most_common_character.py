# Write your solution here
def most_common_character(stringa: str):
    common = stringa[0]
    for char in stringa:
        if stringa.count(char) > stringa.count(common):
            common = char
    return common
    

if __name__ == "__main__":
    second_string = "xemplaryelementary"
    print(most_common_character(second_string))
