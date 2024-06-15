def work(a) :
  stu={0:1}
  r=1
  for x in range(1,a+1):
    for i in range(x,x+1):
      r=r*i
      stu[x]=r
  return stu

	

a = int(input())
ans = work(a)
print(ans)

