a = eval(input())
lst = list(a)
n,m = eval(input())
if -len(lst) <= n < len(lst):
    clst = [lst[n]]*3
    lst.extend(clst)
    print(lst)
else:
    print("error")
