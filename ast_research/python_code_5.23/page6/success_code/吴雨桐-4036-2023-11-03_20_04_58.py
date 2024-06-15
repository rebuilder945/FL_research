n=eval(input())
if n>36:
    print("error")
elif 0<n<11:
    if n%2==0:
        print("black")
    else:
        print("red")
elif 10<n<19:
    if n%2!=0:
        print("black")
    else:
        print("red")
elif 18<n<29:
    if n%2==0:
        print("black")
    else:
        print("red")
elif 28<n<37:
    if n%2!=0:
        print("black")
    else:
        print("red")
else:
    print("green")
