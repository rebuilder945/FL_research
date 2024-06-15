def work(a) :
      jc = 1 
      dic = {0:1}
      for x in range(1,a+1):
        for i in range(1,x+1): 
            jc *= i
        dic[x] = jc
      return  dic

	

a = int(input())
ans = work(a)
print(ans)

