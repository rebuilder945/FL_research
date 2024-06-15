D = {}
for i in range(26):
    D[chr(ord("A")+i)] = chr(ord("A")+25-i)
    D[chr(ord("a")+i)] = chr(ord("a")+25-i)
s = input()
n = ""
for i in s:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        n += D[i]
    else:
        n += i
print(s)
print(n)
