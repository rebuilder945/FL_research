lst=eval(input())
lst1=[]
b=lst.count(0)
for x in lst:
    if x!=0:
        lst1.append(x)
h=[0]*b
lst1.append(h)
print(lst1)
        

