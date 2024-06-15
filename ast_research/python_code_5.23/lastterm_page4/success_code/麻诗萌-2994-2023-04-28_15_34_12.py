lst=input().split(",")
n,m=eval(input())
if n<len(lst):
    s=lst[n]
    lst1=[s]*m
    print(lst+lst1)
else:
    print("error")

