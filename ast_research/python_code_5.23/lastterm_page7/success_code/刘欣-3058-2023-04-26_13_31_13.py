str1=input() or "q"
ls=[]
while str1!="q":
    ls.append(str1)
    str1=input() or "q"
for i in ls:
    if ls.count(i)>1:
        str2=i
    print("%s %d"%(str2,ls.count(i)))
