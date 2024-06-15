nation=input() or "ok"
dic={}
while nation != "ok":
    nation=nation.split()
    dic[nation[0]]=dic.get(nation[0],0)+int(nation[1])
    nation=input() or "ok"
print(list(dic.keys()).sort())
print(list(dic.values()).sort())
if "India" in dic.keys():
    print("yes")
else:
    print("no")
print(sum(dic.values()))

