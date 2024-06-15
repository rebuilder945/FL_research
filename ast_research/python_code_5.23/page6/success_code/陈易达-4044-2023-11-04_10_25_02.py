def is_narcissistic_number(n):
    if len(str(n)) != 3:
        return False
    return sum(int(digit) ** 3 for digit in str(n)) == n

n = int(input())
n2 = None

for i in range(100,n+1):
    if is_narcissistic_number(i):
        n2 = i
        break

if n2 is None:
    print("none")
else:
    print(n2)

