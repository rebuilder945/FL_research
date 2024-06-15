def work(a) :
    dic = {0:1}
    b = 1
    for i in range(1,a+1):
        b*=i
        dic[i] = b
    return dic
	

a = int(input())
ans = work(a)
print(ans)

