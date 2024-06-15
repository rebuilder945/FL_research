lst=input().split(",")
n,m=eval(input())
if n>len(lst):
    print("error")
else:
    lst1=lst[n-1]*m
    lst2=lst+lst1
    print(lst2)
