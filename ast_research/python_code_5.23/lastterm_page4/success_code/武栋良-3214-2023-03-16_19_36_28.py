ls = eval(input())
a = ls.count(0)
while 0 in ls:
    ls.remove(0)
ls1 = [0]*a
ls2 = ls+ls1
print(ls2)
