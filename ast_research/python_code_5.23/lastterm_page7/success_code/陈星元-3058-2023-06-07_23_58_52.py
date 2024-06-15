str=input()
dic={}
while str!="q":
    dic[str]=dic.get(str,0)+1
    str=input()
ls=list(dic.items())
ls.sort(key=lambda x:x[1])
print("{} {}".format(ls[-1][0],ls[-1][1]))


