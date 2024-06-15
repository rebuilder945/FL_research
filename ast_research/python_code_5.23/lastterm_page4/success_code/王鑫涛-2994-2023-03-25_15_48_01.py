a=input().split(',')
b=input().split(',')
p = eval(b[0])
q = eval(b[1])
if p <0 :
    p+=len(a)
else:
    pass
c=[]
for x in a:
    c.append(eval(x))
if p in list(range(len(a))):
    for i in range(q):
        c.append(c[p])
    print(c)
else:
    print('error')

