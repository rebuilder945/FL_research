def work(a) :
  res = {}
    result = 1
    for i in range(a + 1):
        if i == 0:
            res[i] = 1
        else:
            result *= i
            res[i] = result
    return res
	

a = int(input())
ans = work(a)
print(ans)

