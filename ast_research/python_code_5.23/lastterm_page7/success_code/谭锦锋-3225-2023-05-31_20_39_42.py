def work(a) :
  dic1 = {0:1}
  b=1
  for i in range(0,a+1):
    for j in range(0,i+1):
      b*=j
    dic1[i]=b
    b =1
  return dic1
	

a = int(input())
ans = work(a)
print(ans)

