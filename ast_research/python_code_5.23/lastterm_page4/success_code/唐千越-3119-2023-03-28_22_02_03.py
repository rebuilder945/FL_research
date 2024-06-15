lst=eval(input())
lst2=[]
for i in range(len(lst)):
    if lst[i:].count(ls[i])!=1:
        lst2.append(ls[i])
print(lst2)
