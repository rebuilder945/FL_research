a=eval(input())
b=0
c=[]
for x in range(101,a+1):
    x=str(x)
    if len(x)==3:
        for y in x:
            y=int(y)
            b=b+y**3
            if b==x:
                c.append(x)
                print(x)
            else:
                continue
    else:
        continue

if len(c)==0:
    print("none")
