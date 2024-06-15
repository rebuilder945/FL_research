ls = list(eval(input()))
n,m = eval(input())
ls1 = []
if -len(ls) <= n <= len(ls)-1:
    for x in range(m):
        ls.append(ls[n])
    ls = ls + ls1
    print(ls)
else:
    print("error")
