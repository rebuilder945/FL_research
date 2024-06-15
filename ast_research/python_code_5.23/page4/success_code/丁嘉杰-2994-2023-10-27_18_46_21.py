ls1=eval(input())
n,m=input().split(',')
b=eval(n)
c=int(m)
a=len(ls1)
if b>a-1:
    print("error")
elif b<a:
    ls2=[ls1[b]]*c
print(ls2) 
