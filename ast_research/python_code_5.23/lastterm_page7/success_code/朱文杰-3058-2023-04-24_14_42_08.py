Str=input() or "q"
dic={}
while Str!="q":
    dic[Str]=dic.get(Str,0)+1
ls=list(dic.values())
for a in ls:
    if a==max(ls) and dic.get(Str)==a:
        print(Str,a)
