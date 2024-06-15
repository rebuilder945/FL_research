lst=eval(input())
n,m=eval(input())
if n<=m and n<=len(lst) and m<=len(lst):
    for i in range(n,m):
        del lst[i]
        print(lst) 
else:
    print("error")
    
    


 
