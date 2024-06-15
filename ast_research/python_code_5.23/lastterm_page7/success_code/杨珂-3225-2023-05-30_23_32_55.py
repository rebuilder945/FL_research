def work(a) :
    dic={0:1}
    s=1
    for i in range(1,a+1):
        for x in range(1,i+1):
            s=s*x
        dic[i]=s
    return dic
  

	

a = int(input())
ans = work(a)
print(ans)

