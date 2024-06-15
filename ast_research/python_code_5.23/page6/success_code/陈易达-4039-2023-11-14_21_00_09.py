ls = list(eval(input()))
n,m = eval(input())
a = len(ls)
if not n > a-1 and not n < -a:
    d = ls[n]
    for x in range(m):
        ls.append(d)
    print(ls)
else:
    print("error")
