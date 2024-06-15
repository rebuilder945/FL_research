def se(s1,s2):
    X = 0
    Y = 0
    if len(s1) == len(s2):
        for i in s1:
            for j in s2:
                if i == j:
                    X += 1
                else:
                    pass
        for k in s2:
            for l in s1:
                if k == l:
                    Y += 1
                else:
                    pass
    if X == Y and X == len(s1):
        return True
    else:
        return False

s1 = input()
s2 = input()
print(s1,s2)
print(se(s1, s2))
