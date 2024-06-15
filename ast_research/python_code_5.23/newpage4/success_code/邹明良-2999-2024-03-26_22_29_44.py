s = input()
n, m = map(int, input().split(","))
ls = s.split(" ")
a = ls[n]
ls[n] = ls[m]
ls[m] = a
print(ls)
