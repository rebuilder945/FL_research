nation=input().split() or "ok"
dic={}
while nation != "ok":
    dic[nation[0]]=dic.get(dic[nation[0]],0)+int(nation[1])
    nation=input().split() or "ok"
print(dic.keys())
print(dic.values())
if "India" in dic.keys():
    print("yes")
else:
    print("no")
print(sum(dic.values()))

