ls = eval(input())
n,m = eval(input())
ls1 = ls.copy()
if abs(n) and abs(m) <= len(ls):
    for i in ls:
        if n<= ls.index(i) < m:
            ls1.remove(i)
    print(ls1)
else:
    print("error")



