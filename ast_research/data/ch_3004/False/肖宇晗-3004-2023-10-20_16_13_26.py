l = eval(input())
l2 = []
for i in range(len(l)):
    if l[i]==2:
        l2.append(l[i])
    elif l[i]>2:
        for j in range(2,l[i]):
            c=l[i]%j
            if c==0:
                break
            else:
                l2.append(l[i])
print(l2)     
                
            

        

            
        
    
        
             
