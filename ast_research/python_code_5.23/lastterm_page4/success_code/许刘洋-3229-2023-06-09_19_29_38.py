a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if b==[]:
    print("False")
else:
    b.sort()
    c=list(map(b,str()))
    print(','.join(c))
