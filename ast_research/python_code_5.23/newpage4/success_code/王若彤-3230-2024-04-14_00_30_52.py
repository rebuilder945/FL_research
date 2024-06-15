numbers=eval(input())
numbers.sort(reverse=True)
if numbers[0]==0:
    print("0")
else:
    for i in numbers:
        print(i,end='')
