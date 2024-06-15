lst=eval(input())
n,m=eval(input())
l=len(lst)
if 0<=n<l or -l<=n<=-1:
    x=lst[n]
    for i in range(m):
        lst.append(x)
    print(lst)
else:
    print("error")
