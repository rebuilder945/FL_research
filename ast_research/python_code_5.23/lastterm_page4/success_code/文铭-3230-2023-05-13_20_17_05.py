ls = eval(input())
a = 0
n = 0
for x in range(len(ls)):
    a = max(ls)
    n+=a*10**(len(ls)-1)
    ls.remove(a)
print(n)
