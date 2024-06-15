ls=eval(input())
n=ls.count(0)
for i in range(n):
    if 0 in ls:
        ls.remove(0)
print(ls+[0]*n)
