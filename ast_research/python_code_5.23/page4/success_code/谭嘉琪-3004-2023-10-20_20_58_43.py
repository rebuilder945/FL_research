a=eval(input())
b=[]
c=a[0]
for i in a:
    if i > c:
        c=i
for k in a:
    for j in range(2,c):
        if (k%j==0):
            break
        else:
            b.append(k)
print(b)
    
        


