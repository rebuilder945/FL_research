def work(a) :
      ans={}
      for i in range(a+1):
        if i==0:
          ans[0]=1
        else:
          ans[i]=1 
          for x in range(i):
            ans[i]*=x+1
      return ans
	

a = int(input())
ans = work(a)
print(ans)

