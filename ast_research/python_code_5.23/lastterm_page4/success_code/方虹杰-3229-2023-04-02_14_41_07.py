a=eval(input())
flag=True
b=[]
for x in set(a):
    if a.count(x)>1:
        flag=False
        
    else:
        flag=True
        b.append(str(x))
if flag:
    b.sort()
    print(",".join(b))
else:
    print(False)

