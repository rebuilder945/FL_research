s = input().split(' ')
n,m = eval(input())
x = s[:]
a = x[n]
b = x[m]
s[n] = b
s[m] = a
print(s)

