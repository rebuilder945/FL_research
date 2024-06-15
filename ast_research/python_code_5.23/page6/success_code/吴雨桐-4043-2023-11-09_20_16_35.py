lst="".join(eval(input()))#why只能这样输入吗
ls=[]
for i in 'abcdefghijklmnopqlstuvwxyz':
    if i in lst:
        print("%s,%d"%(i,lst.count(i)))
