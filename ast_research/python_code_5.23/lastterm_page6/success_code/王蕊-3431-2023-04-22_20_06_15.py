a=eval(input())
if 1<=a<=10 and 19<=a<=28:
    if a%2!=0:
        print("red")
    else:
        print("black")
elif 11<=a<=18 and 29<=a<=36:
    if a%2!=0:
        print("black")
    else:
        print("red")
elif a==0:
    print("green")
else:
    print("error")

