lst=eval(input())
n,m=eval(input())
lst1=lst.copy()
if n>len(lst)-1 or m>len(lst)-1:
    print("error")
else:
    for i in range(n,m):
        del lst1[i]
        print(lst1) 
   
    
    


 
