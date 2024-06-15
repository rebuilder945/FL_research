def Fibonacci(num,n):
	num=[a,b]
	for x in range(n):
		a,b=b,a+b
		num.append(b)
	return(num[n-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


