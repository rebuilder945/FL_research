namelist = input().split(",")
scorelist = input().split(",")
lst = []
dic = {}
for i in range(len(namelist)):
    dic[namelist[i]] = scorelist[i]
dic = sorted(dic.values())         #注意sorted的返回值是list
for i in dic:
    lst.append(list(i))
print(lst)
