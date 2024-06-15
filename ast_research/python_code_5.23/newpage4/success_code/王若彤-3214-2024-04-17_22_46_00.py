numbers=eval(input())
for i in numbers:
    if i==0:
        numbers.remove(i)
        numbers.append(0)
print(numbers)
