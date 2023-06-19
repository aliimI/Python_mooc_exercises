# Write your solution here
def no_vowels(my_string: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in my_string:
        if char in vowels:
            my_string = my_string.replace(char, "")
    return my_string


if __name__ == "__main__":
    stringa = "this is an example"
    print(no_vowels(stringa))