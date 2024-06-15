a=list(input().split(","))
k=eval(input())
lens=len(a)
c=[]
for x in range (lens):
    a1=a[x]
    b1=k[x]
    c1=["%s,",b1 %(a1)]
    c.append(c1)
print(c)

