namelist = input().split(",")
scorelist = input().split(",")
lst = []
dic = {}
for i in range(len(namelist)):
    dic[namelist[i]] = scorelist[i]
dic = dict(sorted(dic.values()))         #注意sorted的返回值是list
for k,v in dic.items():
    lst.append([k,v])
print(lst)
