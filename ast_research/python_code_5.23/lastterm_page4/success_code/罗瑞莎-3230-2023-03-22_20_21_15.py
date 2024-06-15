s = eval(input())
s.sort()
sum = 0
for i in s:
    a = i*10**(s.index(i))
    sum += a
print(sum)
