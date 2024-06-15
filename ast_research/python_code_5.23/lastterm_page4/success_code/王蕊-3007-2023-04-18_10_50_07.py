lst=eval(input())
n,m=input().split(",")
n=int(n)
m=int(m)
k=len(lst)
if n<k and m<k:
    if n<m:
        del lst[n:m]
        print(lst)
    else:
        del lst[m+1:n+1]
        print(lst)
else:
    print("error")
    

