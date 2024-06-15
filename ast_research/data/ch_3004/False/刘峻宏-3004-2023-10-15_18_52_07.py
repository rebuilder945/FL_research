a=eval(input())
i=0
b=[]
for i in range(len(a)):
    n=a[i]
    m=0
    for x in range (2,n):
        
        if n%x==0:
            m=m+1
            break
        if m==0:    
            b.append(n)

    
print(b)
