p=eval(input())
k=p
for i in k:
    if  p.count(i)>1:
        p.remove(i)    
    else:
        pass
print(p)
