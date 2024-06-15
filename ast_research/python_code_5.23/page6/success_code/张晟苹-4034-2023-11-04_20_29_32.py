def hunhe(m,n):
    if m=='red'and n=='blue':
        return 'purple'
    if m=='red' and n=='yellow':
        return 'orange'
    if m=='blue' and n=='yellow':
        return 'green'
a=input()
b=input()
c=['red','blue','yellow']
if a not in c or b not in c or a==b:
    print('error')
else:
    if hunhe(a,b):
        print(hunhe(a,b))
    else:
        print(hunhe(b,a))


