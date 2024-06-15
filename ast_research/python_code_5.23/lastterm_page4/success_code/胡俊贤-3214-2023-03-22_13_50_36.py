ls=eval(input())
n=ls.count('0')
for i in range(n):
    ls.remove('0')
    ls.insert(-1,'0')
print(ls)


