l = eval(input())
l2 = []
for i in range(len(l)):
    n = l[i]
    if n<=2:
        l2.append(n)
    else:
        c=n%2
        if c==1:
            l2.append(n)
print(l2)

            
        
    
        
             
