numbers = eval(input())
unique_numbers = [num for num in set(numbers) if numbers.count(num) == 1]
if unique_numbers:
    unique_numbers.sort()
    print(",".join(map(str, unique_numbers)))
else:
    print("False")


