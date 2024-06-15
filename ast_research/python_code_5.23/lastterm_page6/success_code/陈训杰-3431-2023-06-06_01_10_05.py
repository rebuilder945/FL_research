n=int(input())
if n<0 or n>36:
    print("error")
elif n==0:
    print("green")
elif n<11:
    if n%2==0:
        print("black")
    else:
        print("red")
elif n<19:
    if n%2==0:
        print("red")
    else:
        print("black")
elif n<29:
    if n%2==0:
        print("black")
    else:
        print("red")
else:
    if n%2==0:
        print("red")
    else:
        print("black")
