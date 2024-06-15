x=eval(input())
b=[]
for a in range(len(x)-1,-1,-1):
    if x[a] not in b:
        b.append(x[a])
print(b.reverse())
    
