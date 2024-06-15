n_E,n_S,n_N,n_O = 0,0,0,0
l = input()
for i in l:
    if "a"<=i<="z"or"A"<=i<="Z":
        n_E += 1
    elif i == " ":
        n_S += 1
    elif "1"<=i<="9":
        n_N += 1
    else:
        n_O += 1
print(n_E,n_S,n_N,n_O)
