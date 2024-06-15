num=eval(input())
if num==0:
    print("green")
if 1<=num<=10 or 19<=num<=28:
    if num%2==1:
        print("red")
    else:
        print("black")
elif 11<=num<=18 or 29<=num<=36:
    if num%2==1:
        print('balck')
    else:
        print("red")
else:
    print("error")

