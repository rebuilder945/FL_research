
    
list=eval(input())
list0=[]
lst1=[]
for x in list:
    for  y in range(2,x**(1/2)):
        if x%y==0:
            list0.append(y)
for x in list0:
    if x not in lst1:
        lst1.append(x)
print(lst1)
