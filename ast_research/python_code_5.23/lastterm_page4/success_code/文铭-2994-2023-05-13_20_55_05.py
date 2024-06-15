l = str(input()).split(',')
ls = [int(x) for x in l]
n,m = eval(input())
if n in range(len(ls)) or range(-len(ls),0):
    for x in range(m):
        ls.append(ls[n])
    print(ls)
else:
    print("error")
