l = str(input()).split(',')
ls = [int(x) for x in l]
n,m = eval(input())
if n <len(ls):
    a = ls[n]
    for x in range(m):
        ls.append(a)
    print(ls)
else:
    print("error")
