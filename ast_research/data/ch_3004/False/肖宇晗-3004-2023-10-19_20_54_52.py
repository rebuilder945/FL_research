l = eval(input())
l2 = []
for i in range(len(l)):
    if l[i]==2:
        l2.append(l[i])
    elif l[i]>2:
        if l[i]%2!=0:
            c=l[i]
            for j in range(2,c):
                if c%j==0:
                    break
        l2.append(l[i])
print(l2)
                
                
            

        

            
        
    
        
             
