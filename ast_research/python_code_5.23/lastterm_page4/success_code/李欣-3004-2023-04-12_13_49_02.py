lst1=eval(input())
lst2=[]
for x in lst1:
    for i in range(2,x):
        if x%i!=0:
           lst2.append(x)
        else:
            break 
if 2 in lst1:
    lst2.append(2)
lst3=sorted(lst2)
print(list(set(lst3)))
