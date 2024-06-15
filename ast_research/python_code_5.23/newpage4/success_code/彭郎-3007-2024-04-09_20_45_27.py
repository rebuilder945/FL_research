lst=eval(input())
n,m=eval(input())
# if n<=m and n in lst and m in lst:
    # for x in range(n,m):
    #     lst=list(lst)
    #     a=lst.pop(x)
if m+1<=len(lst) and n<=m:
    del lst[n :m]
    print(lst)
else:
    print("error")
