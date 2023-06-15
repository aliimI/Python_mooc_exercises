numbers = []
sum_numbers = 0
positive_count = 0
negative_count = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    num = int(input("Number: "))
    
    if num == 0:
        break

    numbers.append(num)
    sum_numbers += num

    count = len(numbers)
    mean = sum_numbers / count

    if num > 0:
        positive_count += 1
    else:
        negative_count += 1


print("Numbers typed in", count)
print("The sum of the numbers is", sum_numbers)
print("The mean of the numbers is ", mean)
print(f"Positive numbers {positive_count}")
print(f"Negative numbers {negative_count}")

