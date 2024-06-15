def work(a) :
    dic = {0:1}
    b = 1
    for i in range(1,a):
        dic[i]=b
        b=b*(i+1)
	

a = int(input())
ans = work(a)
print(ans)

