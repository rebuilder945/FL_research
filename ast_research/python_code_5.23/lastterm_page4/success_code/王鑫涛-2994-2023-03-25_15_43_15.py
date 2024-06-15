a=input().split(',')
b=input().split(',')
c=[]
for x in a:
    c.append(eval(x))
if int(b[0])-1 in list(range(len(a))):
    for i in range(int(b[1])):
        c.append(c[int(b[0])-1])
    print(c)
else:
    print('error')

