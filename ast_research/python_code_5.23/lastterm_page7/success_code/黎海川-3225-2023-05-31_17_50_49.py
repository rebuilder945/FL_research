def work(a) :
    sum=1
    for i in range(1,a + 1):
        sum*=i
    return sum
    
	

a = int(input())
ans = work(a)
print(ans)

