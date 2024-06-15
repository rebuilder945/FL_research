a=list(eval(input()))
if len(a)<=1:
    print([])
elif len(a)>1:
    b=max(a)
    x=a.count(b)
    for i in range(0,x):
        a.remove(b)
    c=min(a)
    y=a.count(c)
    for i in range(0,y):
        a.remove(c)
    print(a)

    
