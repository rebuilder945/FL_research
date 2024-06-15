lst = eval(input())
n,m=eval(input())
if len(lst)-1<m or n>m:
    print("error")
else:
    for x in range(n,m):
        lst.remove(lst[x])
    print(lst)
