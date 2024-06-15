a = input().split(" ")
c=[]
d=[]
while a != 'ok':
    c.append(a[0])
    d.append(eval(a[1]))
    a=input().split(' ')   
c.sort()
d.sort()
print(c)
print(d)
if 'India' in c:
    print('yes')
else:
    print('no')
print(sum(d))

