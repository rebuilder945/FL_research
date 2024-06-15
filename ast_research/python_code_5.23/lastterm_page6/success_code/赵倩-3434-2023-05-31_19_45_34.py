


a=input()
b=input()
r="red"
l="blue"
g="green"
if a!=r and a!=l and a!=g and b!=r and b!=l and b!=g and a==b:
    print("error")
else:
    if (a==r and b==l) or (a==l and b==r):
        print("purple")
    elif (a==l and b==g) or (a==g and b==l):
        print("orange")
    else:
        print("green")
