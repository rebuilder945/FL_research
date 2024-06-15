a=eval(input())
a.sort(reverse=True)
b=len(a)
evn=0
while b>0:
    evn=evn+a[0]*b
    a.remove(a[0])
    b-=1
print(evn)

