def work(a) :
    impor math
    dic=dict()
    for i in range(1,a + 1):
        dic=factorial(i)
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

