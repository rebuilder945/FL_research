def ss(n):
    for x in range(2,n//2+1):
        if n%x==0:
            return False
    return True    
a=eval(input())
b=[]
for x in a:
    if ss(x):
        b.append(x)
for x in b:
    if x==1:
        b.remove(1)  
    if x==0:
        b.remove(0)
print(b)        
