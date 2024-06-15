str=input()
dic={}
while str!="q":
    dic[str]=dic.get(str,0)+1
ls=list(dic.items())
ls.sort(key=lambda x:x[1])
print("{} {}".format(ls[0][0],ls[0][1]))


