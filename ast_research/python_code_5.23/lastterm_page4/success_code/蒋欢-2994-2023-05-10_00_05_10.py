def repeat(ls,n,m):
    if n>=(-len(ls)) and n<(len(ls)):
        for i in range(m):
            ls.append(ls[n])
        print(ls)
    else:
        print("error")
ls=list(eval(input()))
n,m=eval(input())
repeat(ls,n,m)
