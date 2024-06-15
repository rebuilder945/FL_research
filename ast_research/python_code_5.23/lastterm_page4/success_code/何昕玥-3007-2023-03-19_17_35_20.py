lst=eval(input())
n,m=map(int,input().split(","))
if n<len(lst) and m<len(lst):
    if n<m:
        del lst[n:m]
        print(lst)
    else:
        del lst[m+1:n+1]
        print(lst)
else:
    print("error")
