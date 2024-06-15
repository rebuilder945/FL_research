lst=eval(input())
n,m=eval(input())
if n<=m and n>=0 and m<=len(lst):
    for x in range(n,m):
        del lst[x]
    print(lst)    
else:
    print("error")        
