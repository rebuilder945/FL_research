a=int(input())
if 1<=a<=10 and a%2==0:
    print("black")
elif 1<=a<=10 and a%2!=0:
    print("red")
elif 11<=a<=18 and a%2==0:
    print("red")
elif 11<=a<=18 and a%2!=0:
    print("black")
elif 19<=a<=28 and a%2==0:
    print("black")
elif 19<=a<=28 and a%2!=0:
    print("red")
elif 29<=a<=36 and a%2==0:
    print("red")
elif 29<=a<=36 and a%2!=0:
    print("black")
else:
    print("green")
