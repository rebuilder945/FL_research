s = input()
n = list(s)
a = input()
for x in range(len(s)):
    if s.find(a) != -1:
        for y in range(len(a)):
            del n[s.find(a)]
    else:
        break
    s = ''.join(x for x in n)
print(''.join(x for x in n))
