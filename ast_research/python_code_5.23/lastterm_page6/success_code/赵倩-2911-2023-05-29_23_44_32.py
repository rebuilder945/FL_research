a=list(input())
b=list(map(int,a))
c=[]
d=[]
l=len(b)
for i in b:
    h=(i+5)%10
    if i in b[:(l//2)]:
        c.insert(0,h)
    else:
        d.insert(0,h)
e=d+c
print("".join(str(x)for x in e))

    

        







