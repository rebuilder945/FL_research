namelist = input().split(",")
scorelist = input().split(",")
lst = []
dic = {}
for i in range(len(namelist)):
    dic[namelist[i]] = scorelist[i]
print(sorted(zip(dic.keys(),dic.values()),key = lambda i:dic[i]))         #注意sorted的返回值是list

