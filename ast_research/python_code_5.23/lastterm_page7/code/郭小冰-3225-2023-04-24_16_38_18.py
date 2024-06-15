def work(a) :
    fac = 1
    for i in range(1, a + 1):
        fac *= i
    dic = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, ... , a: a * fac}
    return dic

	

a = int(input())
ans = work(a)
print(ans)

