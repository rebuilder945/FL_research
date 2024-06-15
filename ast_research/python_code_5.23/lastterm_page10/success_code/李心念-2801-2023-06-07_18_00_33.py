s = input()
print(s)
num = 0
low = 0
upp = 0
len = 0
spe = 0
for x in s:
    if '0'<= x <='9':
        num = 1
    elif 'a'<= x <='z':
        low = 1
    elif 'A'<= x <='Z':
        upp = 1
    else:
        spe = 1
if len(s) >= 8:
    len = 1
print(num+low+upp+len+spe)
