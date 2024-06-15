lst = list(eval(input()))
n,m = eval(input())
d = len(lst)
if n >= d or n < -d:
    print("error")
else:
    append_l=[lst[n]]*m
    lst=lst+append_l
    print(lst)
