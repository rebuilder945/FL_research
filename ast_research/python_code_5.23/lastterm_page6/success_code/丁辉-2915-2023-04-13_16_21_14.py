a=eval(input())
b=[]
f=[]
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            c=x*100+y*10+z
            d=x**3+y**3+z**3
            if c==d:
                b.append(c)
for e in b:
    if e<=a:
        f.append(e)
        print(len(f))
    if e>a:
        print("none")
