lst=eval(input())
n,m=eval(input())
if n<=m<(len(lst)-1):
    for x in range (n,m):
        del lst[x]
    print(lst)
else:
    print("error")

    
