dct = {}
strTT = input()
lstS = strTT.split()
#为每一个字符串创建键值对
for strT in lstS:
    dct[strT] = dct.get(strT,0) + 1
#找到出现次数最大值
maxV = max(dct.values())
lstK = []
#将所有出现次数为最大值的键装入列表
for k in dct.keys():
    if dct[k] == maxV:
        lstK.append(k)
#对列表进行排序
lstK.sort()
#输出键值对
for k in lstK:
    print(k,dct[k])
