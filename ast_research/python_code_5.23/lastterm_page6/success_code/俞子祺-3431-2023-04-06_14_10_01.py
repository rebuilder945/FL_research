a=eval(input())
if a in range(1,10) or a in range(19,28):
    if a%2==0:
        print("black")
    else:
        print("red")
elif a in range(11,18) or a in range(19,36):
    if a%2==0:
        print("red")
    else:
        print("balck")
elif a==0:
    print("green")
else:
    print("error")

