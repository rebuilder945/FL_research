a=eval(input())
d=0
c=[]
for i in range(100,a+1):
    i=str(i)
    for x in i:
        x=int(x)
        for y in i:
            y=int(y)
            for z in i:
                z=int(z)
                if x**3+y**3+z**3==int(i) and x>0 and i not in c and x!=y and x!=z and y!=z:
                    c.append(i)
                    d=1
if d==0:
    print("none")
else:
    for m in range(len(c)):
        print(c[m])
