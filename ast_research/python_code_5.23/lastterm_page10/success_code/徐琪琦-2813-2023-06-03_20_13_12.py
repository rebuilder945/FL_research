s = list(input())
a = input()

s1 = s[:]
i = 0

while i < len(s1):
    if s1[i:i + len(a)] == list(a):
        del s1[i:i + len(a)]
    else:
        i += 1

print("".join(s1))

