def work(a) :
   s = 1
   t = 1    
   b = {0:1}
   for x in range(1,a+1):
      s= x*s
      b[x] = s
   return b
        
	

a = int(input())
ans = work(a)
print(ans)

