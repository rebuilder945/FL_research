m=str(input())
dict={}
n=[]
while m!='q':
    n.append(m)
    m=str(input())
for key in n: #把list中的单词，作为字典中的key（在字典中key是唯一的），把遍历到key的次数，作为value；
    if dict.get(key) == None: #在字典中查找key，因为创建的是空字典，每个key第一次get结果都是None
        dict[key] = 1 #（key来自list，绝对是字符串中的单词）第一次遍历到key的时候，get结果是None，在空字典中创建该key的键值对，key：1；在后续的遍历过程中，如果再次遍历到这个key，get结果不是None了
    else:
        dict[key] += 1 #遍历到某个key，已经在字典里存在了，就把次数+1
m=max(dict.keys(),key=(lambda x:dict[x]))
print(m,dict[m]) #返回要统计的单词出现次数

