
x=eval(input())
b=str(x)
c=[]
d=0
for i in range(len(b)):
    c.append(b[i])
for i in range(len(c)):
    d+=int(c[i])**3
e=[]
for i in range(100,x):
    if i==d:
        print(i)
        e.append(i)
if e==[]:
    print("none")
    

