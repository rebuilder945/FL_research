def work(a) :
   s = 1
   t = 1
   b = {}    
   for x in range(a+1):
      s= (x+1)*s
      b[x] = s
   return b
        
	

a = int(input())
ans = work(a)
print(ans)

