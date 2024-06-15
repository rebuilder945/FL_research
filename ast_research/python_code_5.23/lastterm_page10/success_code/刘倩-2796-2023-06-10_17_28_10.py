s = input()
shuzi = []
zuichang = []
for x in s:
        if x.isdigit():
                shuzi.append(x)
                if len(shuzi)>=len(zuichang):
                        zuichang = shuzi.copy()
        else:
                shuzi = []
if len(zuichang) > 0:
        print("".join(zuichang))
else:
        print("No digits")
