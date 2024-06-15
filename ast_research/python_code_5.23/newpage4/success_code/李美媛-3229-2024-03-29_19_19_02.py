lst=eval(input())
lst1=[]
lst2=[]
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
    else:
        lst2.append(i)
lst1.sort()
if len(lst2)==len(lst):
    print(False)
else:
    print((',').join(str(i)for i in lst1))

