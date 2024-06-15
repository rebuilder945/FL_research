numbers=eval(input())
for x in numbers:
    for i in range(2,x//2+1):
        if x%i==0:
            numbers.remove(x)
print(numbers)

