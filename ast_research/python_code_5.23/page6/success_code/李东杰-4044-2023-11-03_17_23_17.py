a=eval(input())
b=0
c=0
for x in range(101,a+1):
    x=str(x)
    if len(x)==3:
        for y in x:
            y=int(y)
            b=b+y**3
        x=int(x)
        if b==x:
            c=1
            print(x)
    else:
        continue

if c==0:
    print("none")
