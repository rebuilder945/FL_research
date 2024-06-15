list0=eval(input())
list0=list(list0)
list1=list0.copy()
for i in list0:
    i=int(i)
    for j in range(2,i):
        if i%j==0:
            list1.remove(i)
            break
for i in list1:
    if i==0:
        list1.remove(i)
for i in list1:
    if i==1:
        list1.remove(i)
print(list1)
