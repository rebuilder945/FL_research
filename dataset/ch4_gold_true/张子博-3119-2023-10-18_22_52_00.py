p=eval(input())
for i in p.copy():
    if  p.count(i)>1:
        p.remove(i)    
    else:
        pass
print(p)
