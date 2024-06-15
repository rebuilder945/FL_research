l = eval(input())
n , m = eval(input())
ls1 = list(l)
ls2 = ls1
ls2[int(m)] = ls1[int(n)]
ls2[int(n)] = ls1[int(m)]
print(ls2)
