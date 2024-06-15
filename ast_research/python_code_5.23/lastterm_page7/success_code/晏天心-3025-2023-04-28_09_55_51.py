#2
s = input().split()
dic = {}      #在外面
for i in s:
    dic[i] = dic.setdefault(i,0) + 1
maxvalue = max(dic.values())
ls = [x for x in dic.keys()]
ls.sort()
for i in (ls):
    if dic[i] == maxvalue:
        print(i,dic[i])

