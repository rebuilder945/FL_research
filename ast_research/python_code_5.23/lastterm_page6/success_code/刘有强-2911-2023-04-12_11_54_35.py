a=input()
b=[]
for x in range(len(a)):
    b.append(int(a[x]))
for i in range(len(b)):
    b[i] = (b[i] + 5) % 10
b.reverse()
for k in b:
    print(k, end='')
