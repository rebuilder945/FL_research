ls = list(eval(input()))
ls1=ls.copy()
n,m = eval(input())
index =[x for x in range(-len(ls),len(ls))]

if n not in index:
    print('error')
else:
    for i in range(m):
        ls1.append(ls[n])
    print(ls1)

