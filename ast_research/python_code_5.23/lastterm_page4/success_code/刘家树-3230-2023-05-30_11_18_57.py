a=eval(input())
l=len(a)
num=0
while l>0:
    m=max(a)
    a.remove(m)
    num+=m*10**(l-1)
    l-=1
print(num)
