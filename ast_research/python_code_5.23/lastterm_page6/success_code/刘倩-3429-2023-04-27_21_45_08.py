s = input()

yingwengeshu = 0
konggegeshu = 0
shuzigeshu = 0
qita = 0

for x in s:
    if x.isalpha():
        yingwengeshu+=1
    elif x.isspace():
        konggegeshu+=1
    elif x.isdigit():
        shuzigeshu+=1
    else:
        qita+=1
