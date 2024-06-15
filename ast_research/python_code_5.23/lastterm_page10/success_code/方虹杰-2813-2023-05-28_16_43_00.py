a=list(input())
b=list(input())
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(" ".join(c))        
