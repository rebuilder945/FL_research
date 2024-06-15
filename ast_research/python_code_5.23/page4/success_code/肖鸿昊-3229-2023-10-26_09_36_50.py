a=eval(input())
b=[]
for i in a: 
    c=a.count(i)
    if c==1:
        b.append(i)
        b.sort()
if b==[]:
    print("False")
else:
    print(*b,sep=",")
