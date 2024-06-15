lst=eval(input())
n,m=eval(input())
l=len(lst)
lst1=[]
for i in lst:
    lst1.append(i)
if -l<=n<l:
    x=lst[n]
    for i in range(m):
        lst1.append(x)
    print(lst)
else:
    print("error")
