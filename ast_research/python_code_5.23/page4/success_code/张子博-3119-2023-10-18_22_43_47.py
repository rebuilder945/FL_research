p=eval(input())
for i in p:
    if  p.count(i)>1:
        p.remove(i)    
    else:
        pass
print(p)
