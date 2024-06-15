a,b=eval(input())
lst=[a,b]
for i in range(3,11):
	a,b=b,a+b
	lst.append(b)
lst=[str(x) for x in lst]
print(' '.join(lst))




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


