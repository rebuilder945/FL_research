encoding='UTF-8'
n=eval(input())
k=2
while k <= n-1:
    r = n % k
    if r == 0:
        k=2
        break

    else:
        k=k+1
if k != 2:

    print(n,"is a prime number")
else:
    print(n,"is not a prime number")


