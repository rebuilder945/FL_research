s = input().split(' ')
n,m = map(int,input().split(' '))
x = s[:]
a = x[n]
b = x[m]
s[n] = b
s[m] = a
print(s)

