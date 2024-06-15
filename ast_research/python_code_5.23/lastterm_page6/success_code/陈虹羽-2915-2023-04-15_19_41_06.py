a=eval(input())
b=[]
c=[]
for x in range(0,10):
    for y in range(0,10):
        for z in range(0,10):
            d=x*100+y*10+z
            if d==x**3+y**3+z**3:
                if d>=100:
                    b.append(d)
for i in b:
    if i<=a:
        c.append(i)
if c==[]:
    print('none')
else:
    for i in c:
        print(i)
