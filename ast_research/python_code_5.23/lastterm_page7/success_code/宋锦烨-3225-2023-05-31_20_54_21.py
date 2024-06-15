def work(a) :
  dic={} 
  for i in range(a+1):
    dic[i]=jiecheng(i)
  return dic


def jiecheng(x):
  if x==1 or x==0:
    return 1
  r=x*jiecheng(x-1)
  return r
	

a = int(input())
ans = work(a)
print(ans)

