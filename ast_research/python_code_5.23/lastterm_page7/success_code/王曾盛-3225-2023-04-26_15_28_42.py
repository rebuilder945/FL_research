def work(a) :
    factorial_dict = {0: 1}
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
        factorial_dict[i] = factorial
    return factorial_dict

	

a = int(input())
ans = work(a)
print(ans)

