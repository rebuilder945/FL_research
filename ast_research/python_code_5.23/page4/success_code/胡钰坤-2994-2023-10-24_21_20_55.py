ls = list(eval(input()))
n,m = eval(input())
if -len(ls) <= n <= len(ls)-1:
    x = ls[n]
    for x in range(m):
        ls.append(ls[n])
    print(ls)
else:
    print("error")
