a = list(map(int,list(str(input()))))
b = []
for k in a:
    s = (k+5)%10
    b.append(s)
for i in range(int(len(b)/2)):
    b[i],b[len(b)-1-i] = b[len(b)-1-i],b[i]
print(''.join(map(str,b)))
