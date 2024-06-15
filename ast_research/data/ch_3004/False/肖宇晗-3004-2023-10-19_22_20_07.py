l = eval(input())
l2 = []
for i in l:
    if i>=2:
        for x in range(2,i):
            if i%x==2:
                break
l2.append(i)
print(l2)     
                
            

        

            
        
    
        
             
