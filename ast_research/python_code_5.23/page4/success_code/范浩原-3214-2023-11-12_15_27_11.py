lst=eval(input())
for x in lst:
    if x==0:
        lst.remove(x)
        lst.append(x)    
    else:
        pass
print(lst)

