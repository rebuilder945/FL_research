lst=eval(input())
for i in lst:
    if i>2:
        for x in range(2,i):
            if i%x==0:
                lst.remove(i)
lst.remove(1)
lst.remove(0)
lst1=lst
print(lst1)
