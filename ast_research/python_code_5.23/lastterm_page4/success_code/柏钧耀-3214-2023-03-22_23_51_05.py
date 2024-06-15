lst=eval(input())
a=lst.count(0)
ls2=[]
for i in range(a):
    ls2.append(0)
    lst.remove(0)
lst.extend(ls2)
print(lst)
