a=input().lower()
b=input().lower()
s={a,b}
x={"red","blue"}
y={"red","yellow"}
z={"blue","yellow"}
scolor={'red','blue','yellow'}
if a not in scolor or b not in scolor or a==b:
    print('error')
elif s==x:
    print('purple')
elif s==y:
    print('orange')
else:
    print('green')
