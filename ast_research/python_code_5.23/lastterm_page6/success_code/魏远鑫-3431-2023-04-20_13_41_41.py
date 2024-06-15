n=eval(input())
if n==0:
    print("green")
elif 0<n<11:
    if n%2==0:
        print("black")
    else:
        print("red")
elif 10<n<19:
    if n%2==0:
        print("red")
    else:
        print("black")
elif 18<n<29:
    if n%2==0:
        print("black")
    else:
        print("red")
elif 28<n<37:
    if n%2==0:
        print("red")
    else:
        print("black")
else:
    print("error")
