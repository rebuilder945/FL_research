lst=eval(input())
lst0=[]
lst1=[]
for x in lst:
    if x == 0:
        lst0.append(x)
for x in lst:
    if x!=0:
        lst1.append(x)
cishu=len(lst0)
for x in range(1,cishu+1,1):
    lst1.append(0)
print(lst1)

