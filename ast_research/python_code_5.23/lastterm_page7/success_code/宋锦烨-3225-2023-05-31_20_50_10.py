def work(a) :
  dic={} 
  for i in a:
    dic[i]=jiecheng(i)


def jiecheng(x):
  if x==1 or x==0:
    return 1
  r=n*jiecheng(n-1)
  return r
	

a = int(input())
ans = work(a)
print(ans)

