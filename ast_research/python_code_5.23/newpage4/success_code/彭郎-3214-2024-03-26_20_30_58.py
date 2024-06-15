lst=eval(input())
i=lst.count(0)
a=[0]*i
while i>0:
    lst.remove(0)
    i=i-1
lst.extend(a)
print(lst)
