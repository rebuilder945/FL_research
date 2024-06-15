def work(a) :
    dict1 = {0:1}
    for i in range(1,a+1):  
        num = 1
        for j in range(i):
            j = j+1
            num *= j
        dict1[i] = num

    return dict1
	

a = int(input())
ans = work(a)
print(ans)

