def work(a) :
    dic = {}
    for i in range(a+1):
        n =1
        for b in range(1,i+1):
            n *= b
        dic[i] =n
    return dic
        
	

a = int(input())
ans = work(a)
print(ans)

