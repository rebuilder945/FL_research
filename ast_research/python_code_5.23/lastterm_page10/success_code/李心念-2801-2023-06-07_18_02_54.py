s = input()
n = [0,0,0,0,0]
for x in s:
    if '0'<= x <='9':
        n[0] = 1
    elif 'a'<= x <='z':
        n[1] = 1
    elif 'A'<= x <='Z':
        n[2] = 1
    else:
        n[3] = 1
if len(s) >= 8:
    n[4] = 1
print(sum(n))
