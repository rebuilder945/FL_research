lst=eval(input())
n,m=eval(input())
lst1=lst.copy()
if n<=m and n<=len(lst)-1 and m<=len(lst)-1:
    for i in range(n,m):
        del lst1[i]
        print(lst1) 
else:
    print("error")
    
    


 
