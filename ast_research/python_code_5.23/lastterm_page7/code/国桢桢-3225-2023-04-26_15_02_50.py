def work(a) :
c = []
b = 1
for i in range(1,a+1):
   b = b*i
   c.append((i,b))
d = dict(c)
return d
  
    
	

a = int(input())
ans = work(a)
print(ans)

