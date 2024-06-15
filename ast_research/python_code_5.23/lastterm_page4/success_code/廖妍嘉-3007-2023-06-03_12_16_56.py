lst=eval(input())
n,m=eval(input())
if len(lst)>n and len(lst)>=m and n<=m:
    for i in range(n,m):
        del lst[i]
        print(lst)
else:
    print("error")

        
