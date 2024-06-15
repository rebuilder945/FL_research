lst = list(eval(input()))
n, m = eval(input())
if -len(lst) <= n <len(lst):
    a = lst[n]
    lst1 = [a]*m
    lst.extend(lst1)
    print(lst)
else:
    print("error")
    



