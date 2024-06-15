ls = input().split(" ")
ls2 = []
dic = {}
ls.sort()
for x in ls:
    a = ls.count(x)
    dic[x] = str(a)
    
a = 0
for i in dic.values():
    if int(i) > a:
        a = int(i)
for i in dic.keys():
    if dic[i] == str(a):
        print("{} {}".format(i,a))



