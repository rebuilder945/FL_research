def work(a) :
    dic = {}
    for x in range(a+1):
        if x == 0:
            dic[0] = 1
        else:
            i = x
            for b in range(1,x):
                x *= b
            dic[i] = x
    return dic

	

a = int(input())
ans = work(a)
print(ans)

