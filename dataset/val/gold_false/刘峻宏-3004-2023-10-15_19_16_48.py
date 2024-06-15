a=eval(input())

b=[]
for i in range(len(a)):
    n=a[i]
    m=0
    
    if n==1:
        continue
    
    else:
        for x in range (2,n):
        
            if n%x==0 :
                m=m+1
                break
            else:
                pass
    if m==0:
        b.append(n)
    
print(b)
