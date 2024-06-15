num = input()
n = []
N = ''
for x in range(len(num)):
    x += 1
    a = int(num[-x])
    a = (a+5)%10
    N += str(a)
print(N)
