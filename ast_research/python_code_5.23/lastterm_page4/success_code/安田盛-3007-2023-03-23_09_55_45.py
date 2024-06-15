lst=eval(input())
n,m=eval(input())
if n<=m<(len(lst)-1):
    for x in range (n+1,m+1):
        if x in lst:
            lst.remove(x)
    print(lst)
else:
    print("error")

    
