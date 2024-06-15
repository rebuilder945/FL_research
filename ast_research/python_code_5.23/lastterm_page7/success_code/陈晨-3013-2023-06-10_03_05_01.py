nation=input().split() or "ok"
dic={}
dicn=[]
while nation != "ok":
    dicn.append(nation)
    #dic[nation[0]]=dic.get(nation[0],0)+int(nation[1])
    nation=input().split() or "ok"
dic=dict(dicn)
print(dic.keys())
print(dic.values())
if "India" in dic.keys():
    print("yes")
else:
    print("no")
print(sum(dic.values()))

