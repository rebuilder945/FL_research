s = input()
n,m = eval(input())
ls = s.split()
a = ls[n]
ls[n] = ls[m]
ls[m] = a
print(ls)
