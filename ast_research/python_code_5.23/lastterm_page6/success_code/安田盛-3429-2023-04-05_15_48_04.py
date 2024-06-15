a=input()
x=0
y=0
z=0
haha=[chr(x)for x in range(65,91)]+[chr(x)for x in range(97,123)]
for i in a:
    if str.isnumeric(i):
        x+=1
    elif str.isspace(i):
        y+=1
    elif i in haha:
        z+=1
w=len(a)-x-y-z
b=[z,y,x,w]
for i in b:
    print(i,end=" ")



     
