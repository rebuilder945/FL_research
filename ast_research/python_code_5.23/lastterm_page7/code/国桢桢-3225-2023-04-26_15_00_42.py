def work(a) :
c = []
b = 1
for i in range(1,a+1):
   b = b*i
   c.append((i,b))
work(a) = dict(c)
  
    
	

a = int(input())
ans = work(a)
print(ans)

