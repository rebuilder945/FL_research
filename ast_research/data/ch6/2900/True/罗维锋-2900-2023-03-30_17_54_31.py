n=eval(input())
b=[]
c=[]
if n==int(n) and n>1:
    for i in range(n):
        for x in range(1,i):
            b.append(i%x)
        if b.count(0)==1:
            i=str(i)
            if i==i[-1::-1]:
                c.append(i)
        b=[]
    d=" ".join(c)
    print(d)
else:
    print("illegal input")
