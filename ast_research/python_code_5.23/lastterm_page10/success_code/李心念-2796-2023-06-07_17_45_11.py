s = list(input())
n = [0 for x in range(len(s))]
for x in range(len(s)):
    if '0'<= s[x] <='9':
        for y in s[x:]:
            if '0'<= y <='9':
                n[x] += 1
            else:
                break
max = max(n)
max1 = len(s)-n[::-1].index(max)-1
print(''.join(i for i in s[max1:max1+max]))
