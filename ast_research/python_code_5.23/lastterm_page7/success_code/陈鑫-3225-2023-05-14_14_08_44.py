def work(a) :
    b={}
    a  =  int(input())
    def jie(x):
        c=1
        for i in range(1,x+1):
            c*=i
        return c
    for i in range(a+1):
        b[i]=jie(i)
        return b
	

a = int(input())
ans = work(a)
print(ans)

