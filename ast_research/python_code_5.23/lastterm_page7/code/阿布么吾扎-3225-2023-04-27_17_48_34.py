def work(a) :
  dic={}
    b=1
    for i in range(0,a+1):
        b=b*i
    dic[a]=b
    return dic
	

a = int(input())
ans = work(a)
print(ans)

