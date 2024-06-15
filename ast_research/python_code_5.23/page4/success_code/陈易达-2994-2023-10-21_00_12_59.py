ls = list(eval(input()))
n,m = eval(input())
a = len(ls)
ls2 = []
if not n > a-1 and not n < -a:
    ls2.append(ls[n])
    ls3 = ls2*m
    ls4 = ls+ls3
    print(ls4)
else:
    print("error")
