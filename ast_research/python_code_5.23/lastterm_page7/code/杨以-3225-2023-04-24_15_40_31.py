def work(a) :
dic={0:1}
fa=1
for i in range(1,a+1):
  fa *=i
  dic[i]=fa
return dic
	

a = int(input())
ans = work(a)
print(ans)

