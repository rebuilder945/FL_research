import copy
s = list(input())
a = input()
ls = []
i = j = 0
flag = True
start = 0
s1 = copy.deepcopy(s)
while i < len(a) and j < len(s):
    if a[i] == s[j]:
        start = j
        if len(a) > len(s) - j - 1:
            break
        else:
            for x in range(len(a) - i - 1):
                i += 1
                j += 1
                if a[i] != s[j]:
                    flag = False
                    break
            if flag:
                s1[start:start + len(a)] = []
    else:
        j += 1
        flag = True

print("".join(s1))

