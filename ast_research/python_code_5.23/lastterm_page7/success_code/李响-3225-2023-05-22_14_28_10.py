def work(a) :
   s = 1
   t = 1
   b = {}    
   if a ==0:
     b = {0:1}
     return b
   else:
    for x in range(a+1):
      s= (x+1)*s
      b[x] = s
   return b
        
	

a = int(input())
ans = work(a)
print(ans)

