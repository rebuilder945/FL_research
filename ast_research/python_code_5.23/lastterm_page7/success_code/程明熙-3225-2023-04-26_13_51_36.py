def work(a) :
 dic={}
 for i in range(0,a):
  if i==0:
   dic[i]=1
  else:
   dic[i]=dic[i-1]*i
 return dic
	

a = int(input())
ans = work(a)
print(ans)

