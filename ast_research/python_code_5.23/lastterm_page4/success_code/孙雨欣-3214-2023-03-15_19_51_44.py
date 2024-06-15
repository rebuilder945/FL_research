def judge(ls1):
    a=ls1.count(0)
    if a ==0:
        print(ls1)
    else:
        for i in range(a):
            ls1.remove(0)
        for i in range(a):
            ls1.append(0)
        print(ls1)
ls1=eval(input())
judge(ls1)

