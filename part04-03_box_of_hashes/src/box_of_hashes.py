# Copy here code of line function from previous exercise
def line(int, str):
    if str == "":
        str = "*"
    print(str[0] * int)


def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 1
    while i <= height:
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
