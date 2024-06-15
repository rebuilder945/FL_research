def work(a) :
    dict1={}
    for i in range(1,a+1):
        for y in range(1,i+1):
            b*=y
        dict1.get("i",b)
    return dict1
	

a = int(input())
ans = work(a)
print(ans)

