Str=input() or "q"
dic={}
while Str!="q":
    dic[Str]=dic.get(Str,0)+1
    Str=input() or "q"
ls=list(dic.values())
for i in dic:
    if dic[i]==max(ls):
        print(i,max(ls))
