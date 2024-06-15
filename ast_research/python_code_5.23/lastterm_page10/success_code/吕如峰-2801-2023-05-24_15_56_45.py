s = input()
while len(s) != 0:
    N = 0
    B = 0
    A = 0
    L = 0
    if len(s) >= 8:
        L = 1
    for a in s:
        if a >= 'A' and a<='Z':
            B = 1
        elif a>='a' and a<='z':
            A = 1
        elif a>='0' and a<='9':
            N = 1
    print(L+A+B+N)
