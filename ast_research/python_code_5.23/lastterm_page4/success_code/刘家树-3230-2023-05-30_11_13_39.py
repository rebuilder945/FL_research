a=eval(input())
l=len(a)
num=0
while l>0:
    m=max(a)
    l.remove(m)
    num+=m*10**l
    l-=1
print(num)
