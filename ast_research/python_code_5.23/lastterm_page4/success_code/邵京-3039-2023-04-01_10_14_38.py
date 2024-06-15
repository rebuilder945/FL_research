numbers=eval(input())
maxnumber=max(numbers)
minnumber=min(numbers)
for i in range(0,len(numbers)):
    if numbers[i]==maxnumber or numbers[i]==minnumber:
        numbers.remove(numbers[i])
print(numbers)

