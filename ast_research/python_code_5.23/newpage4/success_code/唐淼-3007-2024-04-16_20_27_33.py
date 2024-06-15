lst=eval(input())
n,m=eval(input())
lst1=lst.copy()
if n<=m and n<=len(lst) and m<=len(lst):
    for i in range(n,m):
        del lst1[i]
        print(lst1) 
else:
    print("error")
    
    


 
