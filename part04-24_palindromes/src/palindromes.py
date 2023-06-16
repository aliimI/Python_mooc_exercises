def palindromes(str):
    return str == str[::-1]

def main():
    while True:
        stringa = input("Type in a word: ")
        if palindromes(stringa):
            print(f"{stringa} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")

main()