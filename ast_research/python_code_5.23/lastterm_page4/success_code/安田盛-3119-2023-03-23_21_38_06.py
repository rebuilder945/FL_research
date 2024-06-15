lst=eval(input())
lst1=lst.copy()
for a in lst:
    b=lst1.count(a)
    if b>1:    
        for i in range(b-1):
            lst1.remove(a)
print(lst1)
        
