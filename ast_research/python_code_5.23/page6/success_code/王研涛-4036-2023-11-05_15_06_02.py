a=eval(input())
if a==0:
    print("green")
elif 1<=a<=10:
    if a%2!=0:
        print("red")
    elif a%2==0:
        print("black")
elif 11<=a<=18:
    if a%2==0:
        print("red")
    elif a%2!=0:
        print("black")
elif 19<=a<=28:
    if a%2!=0:
        print("red")
    elif a%2==0:
        print("black")
elif 29<=a<=36:
    if a%2==0:
        print("red")
    elif a%2!=0:
        print("black")
else:
    print("error")
