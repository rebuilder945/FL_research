n=int(input())
b=[]
d=[]
for i in range(1,n):
    for x in range(1 ,n):
        while i>x:
            if i/x!=i%x:
                b.append(i)
for c in b:
    if b.count(c)==1:
        c.append(c)
        if c!=[]:
           print("".join(map(int,c)))
        elif c==[]:
            print("illegal input")

