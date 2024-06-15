lst=eval(input())
lst0=lst.copy()
for i in lst:
    if lst.count(i)>1:
        lst0.remove(i)
print(lst0)
    
        
