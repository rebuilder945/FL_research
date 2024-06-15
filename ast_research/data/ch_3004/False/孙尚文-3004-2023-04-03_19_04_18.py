a=eval(input())
b=a.copy()
for x in a:
    if x==0 or x==1:
        b.remove(x)
else:
    for y in range(2,x):
        if x%y==0:
            b.remove(x)
            break
print(b)
        
