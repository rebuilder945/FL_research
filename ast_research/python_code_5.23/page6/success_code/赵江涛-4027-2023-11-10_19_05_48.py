n = 0
sum = 0
t=1
while(t):
    a = input()
    if a != '#':
        n+=1
        sum +=int(a)
    else:t=0
print(n,sum)

