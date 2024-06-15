def work(a) :
      js = 0
      jc = 1 
      dic = {0:1}
      for x in range(1,a+1):
            js = x
            while js!=1:
               jc *= js
               js -= 1 
            dic[x] = jc
    return  dic

	

a = int(input())
ans = work(a)
print(ans)

