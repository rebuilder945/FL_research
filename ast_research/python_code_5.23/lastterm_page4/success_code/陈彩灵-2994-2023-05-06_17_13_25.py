ls = list(eval(input()))

n,m = eval(input())
index =[x for x in range(len(ls))]
index.append(-1)
if n not in index:
    print('error')
else:
    for i in range(m):
        ls.append(ls[n])
    print(ls)
