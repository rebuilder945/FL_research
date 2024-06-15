#口袋
a=int(input())
b=a%2
if a!=0:
    for a in range(1,11):
        if b==1:
            print("red")
        elif b==0:
            print("black")
    for a in range(19,29):
        if b==1:
            print("red")
        elif b==0:
            print("black")
    for a in range(11,19):
        if b==1:
            print("black")
        elif b==0:
            print("red")
    for a in range(29,37):
        if b==1:
            print("black")
        elif b==0:
            print("red")
elif a==0:
    print("green")
else:
    print("error")

