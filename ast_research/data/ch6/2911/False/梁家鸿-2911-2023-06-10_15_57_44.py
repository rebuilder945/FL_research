a = input()
a = a[::-1]
sum = 0
for x in a:
    b = a.index(x)
    x = (int(x) + 5)%10
    sum = sum + x * (10**(len(a)-b-1))
print(sum)
