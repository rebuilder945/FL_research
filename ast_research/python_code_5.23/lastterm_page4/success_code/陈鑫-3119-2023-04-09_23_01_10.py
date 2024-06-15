x=eval(input())
for a in range(len(x)):
    while(x.count(x[a])>1):
        x.remove(a)
print(x)
    
