ls = list(eval(input()))
ls1 = []
n,m = eval(input())
if -len(ls) <= n <= len(ls)-1:
    ls1.append(ls[n])
    ls2 = ls1*m
    ls3 = ls+ls2
    print(ls3)
else:
    print('error')
