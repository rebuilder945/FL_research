d = {}
for i in range(26):
    d[chr(ord('A')+i)] = chr(ord('A')+25-i)
    d[chr(ord('a')+i)] = chr(ord('a')+25-i)
m = input()
c = ''
for i in m:
    if 'a'<= i <= 'z' or 'A' <= i <= 'Z':
        c += D[i]
    else:
        c += 1
print(m)
print(c)

