lst=eval(input())
c=""
lst1=[]
for x in lst:
    c=c+x
lst0=list(c)
print(lst0)
for x in lst0:
    if x not in lst1:
        lst1.append(x)
lst1.sort()

for x in lst1:
    b=str(lst0.count(x))
    c=x+","+b
    print(c)
    
