n=eval(input())
if n==0:
    print("green")
elif 0<n<11 or 20<n<29:
    if n%2==0:
        print("black")
    else:
        print("red")
elif 10<n<19 or 28<n<37:
    if n%2==0:
        print("red")
    else:
        print("black")
else:
    print("error")
