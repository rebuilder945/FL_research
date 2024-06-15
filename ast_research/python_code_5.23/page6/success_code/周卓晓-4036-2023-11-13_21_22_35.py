a=eval(input())
if a==0:
    print("green")
elif 1<=a<=10 or 19<=a<=28:
    if a%2==1:
        print("red")
    elif a%2==0:
        print("black")
elif 11<=a<=18 or 29<=a<=37:
    if a%2==0:
        print("black")
    elif a%2==0:
        print("red")
else:
    print("error")


