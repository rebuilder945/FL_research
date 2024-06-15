def lst(a):
    b = a.count(0)
    c =[0]
    while 0 in a:
        a.remove(0)
    for i in range(b):
        a = a+c
    print(a)
a = eval(input())
lst(a)
