op1 = input()
op2 = input()
flag = True
for s in op1:
    if (s not in op2) or (len(op1) != len(op2)):
        flag = False
print(flag)

