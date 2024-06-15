def tongji(ls):
    lsStr="".join(ls)
    ls2=[]
    lsStr2=sorted(lsStr,key=lambda x:ord(x),reverse=False)
    for x in lsStr2:
        if x not in ls2:
            ls2.append(x)
            print("%s,%d"%(x,lsStr2.count(x)))
        else:
            pass

ls=eval(input())
tongji (ls)
