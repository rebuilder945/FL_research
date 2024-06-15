from calendar import c


a=eval(input())
s=a.count(0)
while a.count(0)>=1:
    a.remove(0)
c-[0]*s
a=a+c
print(a)
