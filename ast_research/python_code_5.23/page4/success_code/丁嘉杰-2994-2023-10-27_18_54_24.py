ls1=eval(input())
ls=[]
n,m=input().split(',')
b=eval(n)
c=int(m)
a=len(ls1)
if b>a-1:
    print("error")
elif b<a:
    ls2=[ls1[b]]*c
    for i in ls1:
        ls.append(i)
    for i in ls2:
        ls.append(i)
    print(ls) 
