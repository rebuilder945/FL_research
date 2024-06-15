lst=input().split(",")
lst1=[int(x) for x in lst]
n,m=eval(input())
if -len(lst1)-1<n<len(lst1):
    for i in range(m):
        a=lst1[n]
        lst1.append(a)
    print(lst1)
else:
    print("error")
