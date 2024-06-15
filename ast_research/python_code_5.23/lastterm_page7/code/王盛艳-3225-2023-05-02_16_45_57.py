def work(a) :
x = 1
for i in range(0,x+1):
    x *= i
return x
	

a = int(input())
ans = work(a)
print(ans)

