n=eval(input())
lst=[]
for i in range(n+1):
    c=i%10
    b=(i//10)%10
    a=i//100
    if i==a**3+b**3+c**3 and a!=0 and i<1000:
        lst.append(i)
if len(lst)!=0:
    for x in lst:
        print(x)
else:
    print('none')

   
          
       
    
    
            

