op1 = input()
op2 = input()
flag = True
for s in op1:
    if (s not in op2) or (op1.count(s) != op2.count(s)):
        flag = False
print(flag)

