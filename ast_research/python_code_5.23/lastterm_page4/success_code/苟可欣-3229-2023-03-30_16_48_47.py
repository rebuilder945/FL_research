ls=eval(input())
b=[]
for x in ls:
    if ls.count(x)==1:
        b.append(x)
    else:
        continue
if b==[]:
    print("False")
else:
    b.sort()
    print(*b,sep=",")
