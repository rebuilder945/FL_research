lst = list(eval(input()))
n,m = eval(input())
if -len(lst) < n <len(lst)-1:
    append_1 = [lst[n]]*m
    lst = lst + append_1
    print(lst)
else:
    print("error")

