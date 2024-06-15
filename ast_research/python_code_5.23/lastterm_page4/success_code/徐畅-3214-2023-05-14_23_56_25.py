lst=eval(input())
lst1=[]
for i in lst:
    if i !=0:
        lst1.append(i)
for i in lst:
    if i ==0:
        lst1.append(i)
print(lst1)
