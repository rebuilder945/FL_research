a = input().split(" ")
c=[]
d=[]
c.append(a[0])
d.append(eval(a[0]))
while a != 'ok':
    a=input().split(' ')
    c.append(a[0])
    d.append(eval(a[0]))
c.sort()
d.sort()
print(c)
print(d)
if 'India' in c:
    print('yes')
else:
    print('no')
print(sum(d))
