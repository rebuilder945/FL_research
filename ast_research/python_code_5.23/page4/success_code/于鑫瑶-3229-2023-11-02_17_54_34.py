def nums(ls):
    ls1=[ls.count(i) for i in ls]
    for n in ls1:
        if n ==1:
            m=ls1.index(n)
            p=ls.pop(m)
            ls.sort()
            print(ls)
        else:
            print("False")
ls=eval(input())

