lst=eval(input())
n,m=eval(input())
if len(lst)-1>n and len(lst)-1>=m:
    for i in range(n,m):
        del lst[i]
        print(lst)
else:
    print("error")

        
