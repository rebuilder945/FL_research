lst=eval(input())
m=lst.count(0)
lst1=[0]*m
for i in range(m):
    lst.remove(0)
print(lst+lst1)    
