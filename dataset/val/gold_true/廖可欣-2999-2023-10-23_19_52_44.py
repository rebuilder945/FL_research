zifu = input()
shuzi = input()
eshuzi = shuzi.split()
n = int(eshuzi[0])
m = int(eshuzi[1])
ezifu = zifu.split()
a = ezifu[n]
b = ezifu[m]
ezifu[n] = b
ezifu[m] = a
print(ezifu)
