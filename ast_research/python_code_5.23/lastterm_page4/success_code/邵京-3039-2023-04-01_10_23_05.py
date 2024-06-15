numbers=eval(input())
maxnumber=max(numbers)
minnumber=min(numbers)
for i in numbers:
    if i==maxnumber or i==minnumber:
        numbers.remove(i)
print(numbers)

