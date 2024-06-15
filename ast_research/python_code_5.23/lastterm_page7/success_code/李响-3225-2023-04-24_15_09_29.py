def work(a) :
   b = []
   s = 1
   t = 1    
   for x in range(a):
      s= (x+1)*s
      b.append(x,s)
   return b
        
	

a = int(input())
ans = work(a)
print(ans)

