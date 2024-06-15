g={}
i=input().split()
a=[]
b=[]

while i !=['ok']:
    a.append(i[0])
    b.append(int(i[1]))
    i=input().split()
b.sort()
a.sort()
print(a)
print(b)
if 'India'not in a:
    print('no')
else:
    print('yes')
print(sum(b))



