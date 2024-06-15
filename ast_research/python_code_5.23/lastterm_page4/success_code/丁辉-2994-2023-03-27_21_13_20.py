lst=eval(input())
n,m=eval(input())
if n<=len(lst):
    lst1=lst+[lst[n]]*m
    print(lst1)
else:
    print("error")
