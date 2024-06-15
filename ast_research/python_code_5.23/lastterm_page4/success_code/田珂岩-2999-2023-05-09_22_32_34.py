ls1 = list(input().split())
n,m = map(int,input().split())
ls = ls1.copy()
if n >= len(ls1) or m >= len(ls1):
    print("error")
else:
    ls[n] = ls1[m]
    ls[m] = ls1[n]
    print(ls)
