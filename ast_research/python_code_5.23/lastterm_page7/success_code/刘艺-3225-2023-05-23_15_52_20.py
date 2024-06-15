def work(a) :
      dic={0:1}
      for x in list(range(0,a+1)):
          m = 1 
          for i in range(1,int(x)+1):
              m = m*i
              dic[x] = m
              return dic

	

a = int(input())
ans = work(a)
print(ans)

