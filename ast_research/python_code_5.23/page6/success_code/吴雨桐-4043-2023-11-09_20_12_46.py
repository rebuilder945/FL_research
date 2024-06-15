lst="".join(eval(input()))#why只能这样输入吗
ls=[]
for i in lst:
    if i not in ls:
        print("%s,%d"%(i,lst.count(i)))
        ls.append(i)
