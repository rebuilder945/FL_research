b=eval(input())
c=max(b)
for x in range(c):
    for v in b:
        if (x!=0 and x!=1 and x!=v and v%x==0) or v<=1:
            b.remove(v)
print(b)
