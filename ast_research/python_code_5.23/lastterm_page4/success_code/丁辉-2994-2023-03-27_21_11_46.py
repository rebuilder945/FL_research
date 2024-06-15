lst=eval(input())
n,m=eval(input())
if n<=len(lst):
    a=lst.pop(n)
    lst1=lst+[a]*m
    print(lst1)
else:
    print("error")
