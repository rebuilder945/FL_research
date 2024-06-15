a=eval(input())
if a>36:
    print("error")
elif a==0:
    print("green")
elif a%2==0:
    if a in range(2,11) or a in range(20,29):
        print("black")
    else:
        print("red")
else:
    if a in range(1,10) or a in range(19,28):
        print("red")
    else:
        print("black")
