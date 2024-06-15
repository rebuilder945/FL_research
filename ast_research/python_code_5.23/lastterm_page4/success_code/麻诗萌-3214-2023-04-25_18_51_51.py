lst=eval(input())
m=lst.count(0)
lst1=[0]*m
print(lst1)
for i in lst:
    if 0 in lst:
        lst.remove(0)
print(lst+lst1)    
