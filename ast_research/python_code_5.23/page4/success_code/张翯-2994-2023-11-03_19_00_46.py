lst=input().split(",")
lst1=[int(x) for x in lst]
lst2=[]
n,m=eval(input())
if -len(lst1)-1<n<len(lst1):
    for i in range(m):
        a=lst1[n]
        lst2.append(a)
    print(lst1+lst2)
else:
    print("error")
