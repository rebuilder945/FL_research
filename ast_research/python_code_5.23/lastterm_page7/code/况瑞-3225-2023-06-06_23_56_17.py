def work(a) :
def  work(a)  :
    b={0:1}
    for x in range(1,a+1):
        for i in range(1,x+1):
            b[x]*=i
    return b
	

a = int(input())
ans = work(a)
print(ans)

