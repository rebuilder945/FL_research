zifu = str(input())
n,m = eval(input())
ezifu = zifu.split()
a = ezifu[n]
b = ezifu[m]
ezifu[n] = b
ezifu[m] = a
print(ezifu)
