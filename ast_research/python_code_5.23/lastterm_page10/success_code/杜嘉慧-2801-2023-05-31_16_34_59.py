m = input()
flag = [False, False, False, False, False]
if len(m) >= 8:
    flag[3] = True
for s in m:
    if s.isdigit():
        flag[0] = True
    if s.isalpha():
        if s.islower():
            flag[1] = True
        if s.isupper():
            flag[2] = True
    if s in ['~','!','@','#','%','^','&','*','(',')','_','=','-','/',',','.','[',']','{','}','|','\\']:
        flag[4] = True
print(sum(flag))

