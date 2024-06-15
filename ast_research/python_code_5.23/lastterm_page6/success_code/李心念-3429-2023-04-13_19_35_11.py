m = input()
n = [x for x in m]
E = 0
B = 0
N = 0
O = 0
for y in n:
    if 'a'<=y<='z' or 'A'<=y<='Z':
        E += 1
    elif y == ' ':
        B += 1
    elif type(eval(y)) == int or type(eval(y)) == float:
        N += 1
    else:
        O += 1
print(E,B,N,O)
