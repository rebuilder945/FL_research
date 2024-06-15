def work(a) :

    a = {0: 1}
    a = 1
    for i in range(1, x+1):
        a*= i
        a[i] = a
    return a

	

a = int(input())
ans = work(a)
print(ans)

