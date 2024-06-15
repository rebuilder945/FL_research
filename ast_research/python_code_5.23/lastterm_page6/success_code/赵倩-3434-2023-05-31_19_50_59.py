a=input()
b=input()
r="red"
l="blue"
y="yellow"
if (a!=r and a!=l and a!=y) or (b!=r and b!=l and b!=y) or a==b:
    print("error")
else:
    if (a==r and b==l) or (a==l and b==r):
        print("purple")
    elif (a==r and b==y) or (a==y and b==r):
        print("orange")
    elif (a==l and b==y) or (a==y and b==l):
        print("green")
