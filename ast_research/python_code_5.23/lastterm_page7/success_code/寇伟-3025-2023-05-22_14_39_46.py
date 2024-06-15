s_ls = input().split()
dic = {}
s_ls.sort()
for s in s_ls:
    dic[s]=s_ls.count(s)
dic = dict(sorted(dic.items(),key = lambda x:x[0]))
for k,v in dic.items():
    if v == max(dic.values()):
        print(k,v)
    

