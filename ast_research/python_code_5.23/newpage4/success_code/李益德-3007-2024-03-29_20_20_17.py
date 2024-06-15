lst=list(eval(input()))
n,m=eval(input())
if -len(lst)<=n<=len(lst)-1 and -len(lst)<=m<=len(lst)-1:
    for i in lst[n:m]:
        lst.remove(i)
    print(lst)
else:
    print("error")
