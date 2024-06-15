def work(a) :
    num = []
    shu = []
    dic = {}
    for i in range(a+1):
        num.append(i)
    for i in range(a+1):
        shu.append(a**i)
    for x in range(a+1):
        dic[num[x]] = dic.get(num[x],0) + shu[x]
    return dic
	

a = int(input())
ans = work(a)
print(ans)

