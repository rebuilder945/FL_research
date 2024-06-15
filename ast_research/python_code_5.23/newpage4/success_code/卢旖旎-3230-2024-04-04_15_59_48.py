a=eval(input())
numbers=list(a)
numbers.sort(reverse=True)
if numbers[0]==0:
    print("0")
else:
    for x in numbers:
        print(x,end='')
