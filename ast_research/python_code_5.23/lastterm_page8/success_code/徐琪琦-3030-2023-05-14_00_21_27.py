namelist = input().split(",")
scorelist = input().split(",")
lst = []
dic = {}
for i in range(len(namelist)):
    dic[namelist[i]] = scorelist[i]
dic = sorted(dic.values())
for k,v in dic.items():
    lst.append([k,v])
print(lst)
