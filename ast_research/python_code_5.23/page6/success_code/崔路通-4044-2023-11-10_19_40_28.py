a=eval(input())
if a<100:
    print("none")
else:
    c=0
    d=[]
    for x in (100,a+1):
        n=str(x)
        for i in range(len(n)):
            c+=eval(n[i])**3
        if c==eval(n):
            d.append(c)
            c=0
        else:
            c=0
    if d==[]:
        print("none")
    else:
        for x in d:
            print(x)

