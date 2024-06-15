def work(a) :
dic = {}
for i in range(0,a):
    dic.setdefault('i','i!')
return(dic)

	

a = int(input())
ans = work(a)
print(ans)

