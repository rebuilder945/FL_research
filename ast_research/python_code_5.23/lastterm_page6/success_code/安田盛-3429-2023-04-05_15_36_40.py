a=input()
haha1=[chr(x)for x in range(65,91)]+[chr(x) for x in range(97,123)]
haha2=[str(chr(x)) for x in range(48,58)]
b=[]
x=0
y=0
for i in a:
    if i in haha1:
        x+=a.count(i)
    elif i in haha2:
        y+=a.count(i)
    elif i == " ":
        z=a.count(i)
w=len(a)-x-y-z
b=[x,z,y,w]
for i in b:
    print(i,end=" ")



     
