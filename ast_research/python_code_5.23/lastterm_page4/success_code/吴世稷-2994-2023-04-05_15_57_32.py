ls = list(eval(input()))
ls1 = []
n,m = eval(input())
if 0<= n <= len(ls):
    ls1.append(ls[n])
else:
    print('error')
ls2 = ls1*m
ls3 = ls+ls2
print(ls3)
