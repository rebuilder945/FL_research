a=input() or "q"
dic={}
while a!="q":
    if a not in dic.keys():
        dic[a]=1
    else:
        dic[a]=dic[a]+1
a=input() or "q"
print(dic)
