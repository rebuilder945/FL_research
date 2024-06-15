ls=eval(input())
a=ls.count(0)
for i in range(a):
    ls.remove(0)
    ls.append(0)
print(ls)
