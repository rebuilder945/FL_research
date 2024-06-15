nums  =  eval(input())
dic = {}
for i in nums:
    for x in i:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
lst = sorted(dic.items(),key=lambda x:x[0])
dic2 = dict(lst)
for k,v in dic2.items():
    print(k+","+str(v))


