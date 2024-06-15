lst=eval(input())
for i in lst:
    if i>2:
        for x in range(2,i):
            if i%x==0:
                lst.remove(i)
                break
if 1 in lst:
    lst.remove(1)
if 0 in lst:
    lst.remove(0)
print(lst)
