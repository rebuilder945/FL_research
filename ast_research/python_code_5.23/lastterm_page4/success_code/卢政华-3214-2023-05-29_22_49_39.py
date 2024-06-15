lst=eval(input())
lst2=lst.copy()
s=[]
for i in lst:
    if i==0:
        s.append(i)
        lst2.remove(0)
print(lst2+s)
