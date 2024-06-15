numbers=eval(input())
numbers.sort(reverse=True)
for i in numbers:
    if numbers[0]==0:
        print("0")
    else:
        print(i,end='')
