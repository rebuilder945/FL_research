
    
list=eval(input())
list0=[]
lst1=[]
for x in list:
    for  y in range(2,int(x**(1/2)),1):
        if x%y==0:
            list0.append(x)
for x in list:
    if x not in list0:
        lst1.append(x)
print(lst1)
