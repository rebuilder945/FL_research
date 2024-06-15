a=eval(input())
b=[]
m=0
for i in a:
    if a.count(i)==1:
        b.append(i)
        m+=1
if m==0:
    print("False")
b.sort()
c=','.join(str(h) for h in b)
print(c)

