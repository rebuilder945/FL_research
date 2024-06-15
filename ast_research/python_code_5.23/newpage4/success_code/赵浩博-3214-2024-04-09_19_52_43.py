a=eval(input())
b=a.copy()
for i in range(len(a)):
    if a[i]==0:  
        b.remove(a[i])
        c=b.append(0)
print(b)
        

        
