s = 0
m = 1
n = 0
while(m):
    α = input()
    if(α != '#'):
        n += 1
        s += int(α)
    else:
        m = 0
print(n,s)
