lst=list(eval(input()))
n,m=eval(input())
if n >= len(lst) or n <= -1*len(lst):
    print("error")
else:
    a=[lst[n]]*m
    rlst=lst+a
    print(rlst)

