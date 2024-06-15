a=eval(input())
b=[]
c=reversed(a)
for x in c:
    if x not in b:
        b.insert(0,x)
print(b)

