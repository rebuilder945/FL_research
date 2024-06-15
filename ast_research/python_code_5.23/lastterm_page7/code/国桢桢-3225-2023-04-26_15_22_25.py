def work(a) :
b = 1
c = [(0,1)]
for i in range(1,a+1):
   b = b*i
   c.append((i,b))
d = dict(c)
return d
  
    
	

a = int(input())
ans = work(a)
print(ans)

