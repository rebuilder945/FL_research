p=eval(input())
for i in range(len(p)):
    if i  in p and p.count(i)>1:
        p.remove(i)    
    else:
        pass
print(p)
