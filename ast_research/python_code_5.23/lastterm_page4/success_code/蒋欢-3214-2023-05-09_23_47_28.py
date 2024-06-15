def ling(ls):
    a=ls.count(0)
    while 0 in ls:
        ls.remove(0)
    for i in range(a):
        ls.append(0)
    print(ls)
ls=eval(input())
ling(ls)
