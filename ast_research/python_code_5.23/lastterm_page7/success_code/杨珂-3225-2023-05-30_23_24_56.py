def work(a) :
    def jc(x):
        if x==1:
            return x
        else:
            return x*jc(x-1)
    dic={}
    for i in range(x+1):
        dic[i]=jc(i)
    return dic
  

	

a = int(input())
ans = work(a)
print(ans)

