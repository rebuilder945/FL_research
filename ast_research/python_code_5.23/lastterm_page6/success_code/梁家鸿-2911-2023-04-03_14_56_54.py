a = list(input())
b = []
for x in a:
    y = eval(x)
    y = (y+5)%10
    b.append(y)
for i in range(len(a)):
    i=i
b[i],b[-i-1] = b[-i-1],b[i]
for c in b:
    print(c,end='')
