# Write your solution here
def anagrams(str1, str2):
    sorted1 = sorted(str1)
    sorted2 = sorted(str2)
    if sorted1 == sorted2:
        return True
    return False
        

if __name__ == "__main__":
    print(anagrams("team", "amet"))