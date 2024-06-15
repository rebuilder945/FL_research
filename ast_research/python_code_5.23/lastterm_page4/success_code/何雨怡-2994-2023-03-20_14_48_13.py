lst=list(eval(input()))
n,m=eval(input())
if 0<=n<len(lst) or 1<=-n<=len(lst):
    choose=[lst[n]]*m
    new=lst+choose
    print(new)
else:
    print("error")
