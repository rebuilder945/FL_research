a=eval(input())
if a<0 or a >36:
    print("error")
elif a==0:
    print("green")
elif 1<=a<=10 or 19<=a<=28:
    if a%2==0:
        print("black")
    else:
        print("red")
else:
    if a%2==0:
        print("red")
    else:
        print("black")
