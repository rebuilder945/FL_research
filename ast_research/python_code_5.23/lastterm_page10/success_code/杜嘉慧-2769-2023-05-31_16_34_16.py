op = input()
ans = list(op)
for i in range(len(op)):
    if op[i].isalpha():
        if op[i].islower():
            ans[i] = chr(26 - (ord(op[i]) - ord('a') + 1) + ord('a'))
        else:
            ans[i] = chr(26 - (ord(op[i]) - ord('A') + 1) + ord('A'))
print(op)
print(''.join(x for x in ans))

