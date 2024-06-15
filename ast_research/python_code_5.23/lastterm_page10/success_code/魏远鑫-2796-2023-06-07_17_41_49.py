x=input()
a=[]
s=''
x += ' '
for i in range(len(x)-1):
    if '0' <= x[i] <= '9':
        s += x[i]
    if len(s)>0 and (x[i+1] > '9' or x[i+1] < '0'):
        a.append(s)
        s=''
b=''
if len(a) == 0:
    print('No digits')
else:
    for i in a:
        if len(i) >= len(b):
            b = i
    print(b)
