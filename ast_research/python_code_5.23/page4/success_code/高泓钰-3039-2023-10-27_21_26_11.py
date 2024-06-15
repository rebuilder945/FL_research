lst=eval(input())
lst2=lst[:]
lst.sort()
max=lst[-1]
min=lst[0]
for i in lst2 :
    if i==max or i==min:
        lst2.remove(i)
print(lst2)


