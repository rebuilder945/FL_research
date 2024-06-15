def work(a) :
    dic = {}
    for i in range(a+1):
        number = 1
        if i == 0:
            number = 1
            dic[str(i)] = number
        else:    
            for s in range(i):
                number = number*(s+1)
            dic[str(i)] = number
    return dic
	

a = int(input())
ans = work(a)
print(ans)

