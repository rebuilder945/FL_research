a=eval(input())
e=True
for i in range(a):
    b=str(i)
    c=len(b)
    d=0
    if c>=3:
        for x in b:
            d+=int(x)**c
        if i==d:
            print(i)
            e=False
if e:
    print('none')
    
    


