numbers=eval(input())
for x in numbers:
    for i in range(2,x,1):
        if x%i==0:
            numbers.remove(x)
        elif x==2:
            continue
        else:
            continue
print(numbers)
