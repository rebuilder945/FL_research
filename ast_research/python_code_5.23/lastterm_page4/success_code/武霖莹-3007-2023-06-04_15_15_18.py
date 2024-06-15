lst = eval(input())
n,m = eval(input())
if -len(lst) <= n < len(lst) and -len(lst) <= m < len(lst):
    ls1 = []
    for i in lst:
        if n <= lst.index(i) < m:
            pass
        else:
            ls1.append(i)
    print(ls1)
else:
    print("error")

