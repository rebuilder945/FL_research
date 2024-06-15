def work(a) :
    dict1={}
    b=1
    for i in range(1,a+1):
        for y in range(1,i+1):
            b*=y
        dict1.setdefault(i,b)
    return dict1

	

a = int(input())
ans = work(a)
print(ans)

