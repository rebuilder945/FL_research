ls1 = eval(input())
a = ls1.count(0)
while 0 in ls1:
    ls1.remove(0)
while a>0:
    ls1.append(0)
    a-=1
print(ls1)
