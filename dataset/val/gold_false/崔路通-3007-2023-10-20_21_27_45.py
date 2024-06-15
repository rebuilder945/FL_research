a=eval(input())
n,m=eval(input())
if n<=m and m<=len(a):
    for x in a[n:m]:
        a.remove(x)
        print(a)
elif n>=m and n<=len(a):
    for x in a[m:n]:
        a.remove(x)
        print(a)
else:
    print("error")




            
        
    
        
    
    

        
        
        
        
            



        
    









