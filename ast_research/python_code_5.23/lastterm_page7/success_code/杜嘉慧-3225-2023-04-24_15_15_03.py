def work(a) :
     ans={0:1}
     for i in range(1,a+1):
          ams[i]=ans.get(i-1)*i#前一个位置的键值*i
     return ans
	

a = int(input())
ans = work(a)
print(ans)

