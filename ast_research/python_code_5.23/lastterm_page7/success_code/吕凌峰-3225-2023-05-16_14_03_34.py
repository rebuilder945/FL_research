def work(a) :
    dic = {}
    for i1 in range(a + 1):
        factorial_a = 1
        if i1 == 0:
            dic[i1] = factorial_a
        else:
            for i2 in range(1, i1 + 1):
                factorial_a *= i2
            dic[i1] = factorial_a
    return dic

	

a = int(input())
ans = work(a)
print(ans)

