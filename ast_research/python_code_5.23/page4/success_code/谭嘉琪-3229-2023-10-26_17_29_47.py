a=eval(input())
ls=[]
m=""
for i in a:
    b=a.count(i)
    if b==1:
        ls.append(i)
if ls==[]:
    print("False")
else:
    ls.sort()
    d=max(ls)
    ls.remove(d)
    for i in ls:
        c=str(i)
        c=c+","
        m=m+c
e=int(d)
n=m+e
print(n)
