nation=input() or "ok"
dic={}
while nation != "ok":
    nation=nation.split()
    dic[nation[0]]=dic.get(nation[0],0)+int(nation[1])
    nation=input() or "ok"
print(dic.keys())
print(dic.values())
if "India" in dic.keys():
    print("yes")
else:
    print("no")
print(sum(dic.values()))

