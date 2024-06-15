m = input()
flag = [0,0,0,0,0]
if len(m) >= 8:
    flag[3] = 1
for s in m:
    if s.isdigit():
        flag[0] = 1
    if s.isalpha():
        if s.islower():
            flag[1] = 1
        if s.isupper():
            flag[2] = 1
    if s in ['~','!','@','#','%','^','&','*','(',')','_','=','-','/',',','.','[',']','{','}','|','\\']:
        flag[4] = True
print(flag.count(1))

