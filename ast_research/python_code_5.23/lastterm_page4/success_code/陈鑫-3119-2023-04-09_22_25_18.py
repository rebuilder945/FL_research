x=input()
for a in x:
    if x.count(a)>1:
        for i in range(x.count(a)-1):
            x.remove(a)
print(x)
    
