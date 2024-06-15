s1=input()
s2=input()
lst=[s1,s2]
a={"red","blue"}
b={"red","yellow"}
c={"blue","yellow"}
color=["red","blue","yellow"]
d=set(lst)
if d==a:
    print("purple")
elif d==b:
    print('orange')
elif d==c:
    print("green")
elif a==b or a not in color or b not in color:
    print("error")
