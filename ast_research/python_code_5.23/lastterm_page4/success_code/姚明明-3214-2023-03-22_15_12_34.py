a=eval(input())
s=a.count(0)
if s>=1:
    a.remove(0)
    c=[0]*s
    a=a+c
else:
    print(a)
