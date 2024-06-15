a = eval(input())
if a <0 or a>36:
    print("error")
elif 1<=a<=10:
    if a%2==0:
        print("black")
    else :
        print("red")
elif 10<a<=18:
    if a%2==0:
        print("red")
    else:
        print("black")
elif 18<a<=28:
    if a%2==0:
        print("black")
    else:
        print("red")
elif 28<a<=36:
    if a%2==0:
        print("red")
    else:
        print("black")
elif a==0:
    print("green")
    


