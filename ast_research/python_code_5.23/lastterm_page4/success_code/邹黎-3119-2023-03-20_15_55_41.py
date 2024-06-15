lst=list(eval(input()))
lst0=[]
for x in lst:
    if lst.count(x)>=2:
        lst0.append(x)
        for x in lst0:
            if lst0.count(x)==2:
                lst0.remove(x)
            if lst0.count(x)==3:
                lst0.remove(x)
                lst0.remove(x)
            if lst0.count(x)==4:
                lst0.remove(x)
                lst0.remove(x)
                lst0.remove(x)
    if x not in lst0:
        lst0.append(x)
                
print(lst0)
    
