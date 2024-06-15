a = input()
dic ={}
res = 0
while(a!="q"):
    dic[a] = dic.get(a,0) + 1
    if dic[a] > res:
        res = dic[a]
    a = input()
for k,v in dic.items():
    if v == res:
        print(k,v)
