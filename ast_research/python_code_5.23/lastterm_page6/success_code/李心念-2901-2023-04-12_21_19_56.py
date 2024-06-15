n = []
x = ''
i = -1
while x != '#':
    x=input()
    i+=1
    if x != '#':
        n.append(eval(x))
print(i,sum(n))
