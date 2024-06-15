def work(a) :
    dic={}
    def jiecheng(s):
        sum=1
        if s==0:
            return 1
        else:
            for i in range(1,s+1):
                sum=sum*i
            return sum
    for m in range(a+1):
        dic[m]=jiecheng(m)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

