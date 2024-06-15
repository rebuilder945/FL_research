a=eval(input())
if a==0:
    print("green")
elif 1<=a<=10 or 19<=a<=28:
    if a//2==0:
        print("black")
    else:
        print("red")
elif 11<=a<=18 or 29<=a<=36:
    if a//2==0:
        print("black")
    else:
        print("red")
else:
    print("error")
