
x=eval(input())
def s(a):
    b=str(a)
    c=[]
    d=0
    for i in range(len(b)):
        c.append(b[i])
    for i in range(len(c)):
        d+=int(c[i])**3
        if a==d:
            return True
        else:
            return False
e=[]
for i in range(100,x):
    if s(i):
        print(i)
        e.append(i)
if e==[]:
    print("none")
    

