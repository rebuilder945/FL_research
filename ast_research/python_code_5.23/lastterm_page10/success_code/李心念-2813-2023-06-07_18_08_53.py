s = input()
a = input()
for x in range(len(s)):
    if s.find(a) != -1:
        for y in range(len(a)):
            del s[s.find(a)]
    else:
        break
print(s)
