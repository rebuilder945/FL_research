lst=eval(input())
n,m=eval(input())
l=len(lst)
if -l<=n<l:
    x=lst[n]
    for i in range(m):
        lst.append(x)
    print(lst)
else:
    print("error")
