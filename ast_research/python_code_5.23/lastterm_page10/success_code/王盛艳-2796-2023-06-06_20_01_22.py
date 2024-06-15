s = input()
l = []
longest = []
for i in range(len(s)):
    if "0" <= s[i] <= "9":
        l.append(s[i])
        if len(l) >= len(longest):
            longest = l.copy()
    else:
        l =[]
if len(longest) > 0:
    print("".join(longest))
else:
    print("No digits")
