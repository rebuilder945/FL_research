N = int(input())
def isPrime(n):
    if n > 1 :
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            return n


def reverseNumber(n):
    num = str(n)
    m = num[::-1]
    if num == m:
        return n


for n in range(1, N + 1):
    if isPrime(n) and reverseNumber(n) == n:
        print(n)
exit(0)

