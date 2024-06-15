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
print(b)        
