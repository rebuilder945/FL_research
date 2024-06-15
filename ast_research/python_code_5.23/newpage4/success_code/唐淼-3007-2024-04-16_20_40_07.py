lst=eval(input())
n,m=eval(input())
if n>len(lst)-1 or m>len(lst)-1:
    print("error")
else:
    for i in range(n,m):
        del lst[i]
    print(lst) 
   
     
    


 
