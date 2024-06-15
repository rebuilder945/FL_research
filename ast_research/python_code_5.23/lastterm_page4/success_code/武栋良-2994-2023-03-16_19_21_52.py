ls = list(map(int,input().split(",")))
n,m = eval(input())
a = len(ls)
if n in range(-a,a):
    ls1 = [ls[n]]
    ls2 = ls1*m
    ls3 = ls+ls2
    print(ls3)
else:
    print("error")

