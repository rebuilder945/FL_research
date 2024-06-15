a=int(input())
if a==0:
    print("green")
elif a in range(1,11):
    if a%2==0:
        print("black")
    else:
        print("red")
elif a in range(11,19):
    if a%2==0:
        print("red")
    else:
        print("black")
elif a in range(1,11):
    if a%2==0:
        print("black")
    else:
        print("red")
elif a in range(1,11):
    if a%2==0:
        print("red")
    else:
        print("black")
else:
    print("error")

