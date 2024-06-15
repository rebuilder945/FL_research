num = eval(input())
if num==0:
    print("green")
elif 1<=num<=10 or 19<=num<=28:
    if num%2==0:
        print("black")
    if num%2==1:
        print("red")
elif 11<=num<=18 or 29<=num<=36:
    if num%2==0:
        print("red")
    if num%2==1:
        print("black")
else:
    print("error")
