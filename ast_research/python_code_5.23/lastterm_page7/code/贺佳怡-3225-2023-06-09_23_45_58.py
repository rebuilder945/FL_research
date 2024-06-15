def work(a) :
      m=list(range(1,a+1))
      b={0:1}
      for i in m:
           sum=1
           c=1
           while c<=i:
                  sum*=c
                  c+=1
            b.setdefault(i,sum)
      return b
	

a = int(input())
ans = work(a)
print(ans)

