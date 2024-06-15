lst=eval(input())
if 1 in lst:

    lst.remove(0)
if 0 in lst:
    lst.remove(1)
a=[]
for i in lst:
    for x in range(2,i):
        if i%x==0:
            break
    else:
        a.append(i)
print(a)
            

