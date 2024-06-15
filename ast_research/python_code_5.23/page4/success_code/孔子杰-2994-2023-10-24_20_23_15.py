lst=input().split(",")
n,m=eval(input())
if n>len(lst) or n<0:
    print("error")
else:
    lst1=lst[n-1]*m
    lst2=lst+lst1
    print(lst2)
