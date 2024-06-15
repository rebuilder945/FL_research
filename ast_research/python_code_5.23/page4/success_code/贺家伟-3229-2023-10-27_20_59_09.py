a=eval(input())
b=[]
c=0
for i in range(0,len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
        b.sort()
if b==[]:
    print("False")
else:
    for i in b:
        c=c+b
        c=eval(c)
    print(c)
