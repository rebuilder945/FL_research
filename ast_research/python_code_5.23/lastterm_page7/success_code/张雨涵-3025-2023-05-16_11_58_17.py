ls = input().split()
dic = {}
for i in ls:
    a = ls.count(i)
    dic.setdefault(i,a)
for b,c in dic.items():
    if c==max(dic.values()):
        print(b,c)
