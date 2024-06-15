s = input()
shuzi = []
zuichang = []

for i in range(len(s)):
    if s[i].isdigit():
        shuzi.append(s[i])
        if len(shuzi)>=len(zuichang):
            zuichang = shuzi.copy()

    else:
        shuzi = []

if len(zuichang) > 0:
    print("".join(zuichang))
else:
    print("No digits")
