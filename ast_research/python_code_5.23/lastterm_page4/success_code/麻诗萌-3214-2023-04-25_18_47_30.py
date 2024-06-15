lst=eval(input())
m=lst.count(0)
lst1=[0]*m
for i in lst:
    lst.remove(0)
print(lst+lst1)    
