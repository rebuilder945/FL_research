s=input()
if s=="":
    print("None")
else:
    for i in range(len(s)):
        if s[i] not in (s[:i]+s[i+1:]):
            print(s[i])

