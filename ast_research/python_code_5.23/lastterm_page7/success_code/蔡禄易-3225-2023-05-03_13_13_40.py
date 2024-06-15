def work(a) :
    dic1 = {}
    for i in range(0,a):
        dic1.setdefault('i','i!')
    return(dic1)

	

a = int(input())
ans = work(a)
print(ans)

