a={"red","blue"}
b={"red","yellow"}
c={"blue","yellow"}
n=input()
l=input()
d=n,l
d=set(d)
if d==a:
    print("purple")
elif d==b:
    print("orange")
elif d==c:
    print("green")
else:
    print("error")

