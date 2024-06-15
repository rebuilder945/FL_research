def work(a) :
    dic = {0:1}
    i=1
    t = 1
    while i <= a:
        t = t*i
        dic.setdefault(i,t)
        i += 1
    return dic
	

a = int(input())
ans = work(a)
print(ans)

