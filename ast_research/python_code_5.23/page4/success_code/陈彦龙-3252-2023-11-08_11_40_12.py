def Fibonacci(num,n):
	for x in range(n):
		num[x],num[x+1]=num[x+1],num[x]+num[x+1]
		num.append(num[x+1])
	return(num[n-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


