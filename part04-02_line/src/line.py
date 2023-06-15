# Write your solution here
def line(int, str):
    if str == "":
        str = "*"
    print(str[0] * int)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")