op = input()
ans = list(op)
for i in range(len(op)):
    if ans[i].isalpha():
        if ans[i].islower():
            ans[i] = chr(26 - (ord(ans[i]) - ord('a') + 1) + ord('a'))
        else:
            ans[i] = chr(26 - (ord(ans[i]) - ord('A') + 1) + ord('A'))
print(op)
print(''.join(x for x in ans))

