def work(a) :
     dic={}
     m=0
     n=1
     while a>=0:
         dic[m]=n
         m+=1
         n=n*(n+1)
         a-=1
     return dic
          
	

a = int(input())
ans = work(a)
print(ans)

