a=eval(input())
n=[]
for i in a:
    x=a.count(i)
    if x==1:
        y=i
        if y not in n:
            n.append(y)
        else:
            break
    else:
        continue
if n==[]:
    print(False)
else:
    n1=sorted(n)
    m1=''
    for m in n1:
        m2=str(m)
        m1=m1+','+m2
    print(m1)
