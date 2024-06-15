lst1=eval(input())
lst2=[]
for x in lst1:
    for i in range(2,x):
        if x%i!=0:
           lst2.append(x)
        else:
            break 
for y in lst2:
    if y%3==0:
        lst2.pop(y)
if 2 in lst1:
    lst2.append(2)
lst3=sorted(set(lst2))
print(list(lst3))
