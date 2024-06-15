def work(a) :

    key1=[]
    value1=[]
    for i in range(a+1):
        key1.append(i)
        result = 1
        for n in range(1, i+1):
            result *= n
        value1.append(result)
    dic=dict(zip(key1,value1))
    return dic
	

a = int(input())
ans = work(a)
print(ans)

