x=eval(input())
b=[]
for a in range(len(x)):
    if x[a] not in b:
        b.append(x[a])
print(b)
    
