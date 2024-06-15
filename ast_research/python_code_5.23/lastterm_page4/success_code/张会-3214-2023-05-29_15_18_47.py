ls=eval(input())
n=ls.count(0)
while 0 in ls:
    ls.remove(0)
for i in range(n):
    ls+=[0]
print(ls)
