# Copy here code of line function from previous exercise
def line(int, str):
    if str == "":
        str = "*"
    print(str[0] * int)

def square(size, character):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "o")