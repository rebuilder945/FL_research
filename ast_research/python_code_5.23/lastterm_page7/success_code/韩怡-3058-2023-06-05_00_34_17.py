s=input() or "q"
dic={}
while s != "q":
    dic[s]=dic.get(s,0)+1
    s=input() or "q"
print(max(s,dic.get),max(dic.values()))

