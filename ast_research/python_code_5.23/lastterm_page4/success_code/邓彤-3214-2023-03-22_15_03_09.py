a=eval(input())
b=[]
for x in a:
    if x!=0:
        b.append(x)
c=a.count(0)
i=0
while i<c:
    b.append(0)
    i+=1
print(b)

