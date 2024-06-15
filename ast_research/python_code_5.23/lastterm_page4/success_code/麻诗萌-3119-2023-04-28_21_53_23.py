lst=eval(input())
for i in lst:
    if lst.count(i)>1:
        for x in range(lst.count(i)):
            lst.remove(i)
print(lst)
    
        
