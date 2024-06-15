def repeat(ls,n,m):
    if n>=(-len(ls)) and n<(len(ls)):
        a=ls[n]
        for i in range(m):
            ls.append(a)
        print(ls)
    else:
        print("error")
ls=list(eval(input()))
n,m=eval(input())
repeat(ls,n,m)
