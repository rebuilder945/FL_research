a = (input())
b = 0
for i in range(len(a)):
    b += ((int(a[i])+5)%10)*(10**i)
print(b)


