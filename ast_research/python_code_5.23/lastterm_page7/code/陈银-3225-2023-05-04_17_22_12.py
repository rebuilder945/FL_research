def work(a) :
    dic={}
    b = 1
    for x in range(a):
        for i in range(1,x+1):
        b *= i
    dic[x]=b
	

a = int(input())
ans = work(a)
print(ans)

