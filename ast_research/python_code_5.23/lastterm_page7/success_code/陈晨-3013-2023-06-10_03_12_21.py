nation=input() or "ok"
dic={}
while nation != "ok":
    nation=nation.split()
    dic[nation[0]]=dic.get(nation[0],0)+int(nation[1])
    nation=input() or "ok"
dk=list(dic.keys())
dk.sort()
dv=list(dic.values())
dv.sort()
print(dk)
print(dv)
if "India" in dic.keys():
    print("yes")
else:
    print("no")
print(sum(dic.values()))

