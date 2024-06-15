def zuzhuang(ls):
    ls.sort(reverse=True)
    ls2=[]
    for x in ls:
        ls2.append(str(x))
    ls3="".join(ls2)
    print(ls3)
ls=eval(input())
zuzhuang(ls)
