num = str(input())
num1 = ''
for i in num:
    n = int(i)
    n = (n+5)%10
    n = str(n)
    num1 += n
print(num1[::-1])

