numbers=eval(input())
for i in numbers:
    if max(numbers)==i:
        numbers.remove(i)
    elif min(numbers)==i:
        numbers.remove(i)
print(numbers)

