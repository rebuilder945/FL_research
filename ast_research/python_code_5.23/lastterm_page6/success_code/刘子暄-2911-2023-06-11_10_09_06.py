a=list(input())
c=[]
for b in a:
    b=str(b)
    b=(b+5)%10
    c.append(b)
d=c.reverse()
print(int(d))
