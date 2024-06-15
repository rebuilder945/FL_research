a=eval(input())
s=a.count(0)
if s>=1:
    b=a.remove(0)
    c=[0]*s
    d=b+c
    print(d)
else:
    print(a)
