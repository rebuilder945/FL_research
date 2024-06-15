ls = input().split()
dic = {}
ls.sort()
# ls1 = []
# for i in ls:
#     i = eval(i)
#     ls1.append(i)
# ls1.sort()
for i in ls:
    a = ls.count(i)
    dic.setdefault(i,a)
for b,c in dic.items():
    if c==max(dic.values()):
        print(b,c)
#没有做到升序排列
