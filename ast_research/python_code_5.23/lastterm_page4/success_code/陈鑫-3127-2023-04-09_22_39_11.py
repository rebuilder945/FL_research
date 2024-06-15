a=[]
n=eval(input())
for i in range(n):
    a.append(i+1)    
for x in range(n-1):
    a[x]=a[x+1]
a[n]=a[0]-1
print(a)
