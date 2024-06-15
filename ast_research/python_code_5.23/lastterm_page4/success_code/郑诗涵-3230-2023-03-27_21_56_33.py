s = eval(input())
s.sort()
sum = 0
for i in range(len(s)):
    a = s[i]*10**(i)
    sum += a
print(sum)

