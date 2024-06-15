def work(a) :
    b = 1
    dic = {}
    for i in range(a):
        dic[i] = b
        b *= (i+1)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

