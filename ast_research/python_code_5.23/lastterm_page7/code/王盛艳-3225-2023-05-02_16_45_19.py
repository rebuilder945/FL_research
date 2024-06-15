def work(a) :
a = 1
for i in range(0,a+1):
    a *= i
return a
	

a = int(input())
ans = work(a)
print(ans)

