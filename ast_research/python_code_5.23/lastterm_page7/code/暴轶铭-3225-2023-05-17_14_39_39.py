def work(a) :
 dic = {0: 1} 
    fact = 1 
    for i in range(1, a+1): 
        fact *= i
        dic[i] = fact
    return dic
	

a = int(input())
ans = work(a)
print(ans)

