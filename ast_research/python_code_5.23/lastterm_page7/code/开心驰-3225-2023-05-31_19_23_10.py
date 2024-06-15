def work(a) :
ans={}
for i in range(a):
  if i=0:
    ans[0]=1
  else:
    for x in range(i):
      ans[x+1]=1
      ans[x+1]*=x

	

a = int(input())
ans = work(a)
print(ans)

