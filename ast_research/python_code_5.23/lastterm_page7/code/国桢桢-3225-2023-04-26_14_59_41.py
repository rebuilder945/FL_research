def work(a) :
lst = [(0,1)]
b = 1
for i in range(1,a+1):
   b = b*i
   lst.append((i,b))
work(a) = dict(lst)
  
    
	

a = int(input())
ans = work(a)
print(ans)

