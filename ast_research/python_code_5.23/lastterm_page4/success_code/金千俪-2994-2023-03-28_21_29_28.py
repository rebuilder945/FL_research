lst=list(eval(input()))
n,m=eval(input())
if n<=len(lst):
    lst = lst+[lst[n]]*m
    print(lst)
else:
    print("error")


