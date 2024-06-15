def is_shuixian(x):
    s = str(x)
    sum = 0
    for c in s:
        sum += int(c) ** 3
    return sum == x

n = int(input())
found = False
for x in range(100, n+1):
    if is_shuixian(x):
        print(x)
        found = True
if not found:
    print("none")

