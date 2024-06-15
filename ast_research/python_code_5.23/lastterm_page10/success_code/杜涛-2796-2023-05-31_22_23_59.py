def f(i):
    if i.isdigit():
        return False
    else:
        return True

a=input()
for i in a:
    if f(i):
        b=a.replace(i,' ')
        a=b
c=list(a.strip().split())
if c==[]:
    print('No digits')
else:
    d=0
    for i in c:
        e=len(i)
        if e>d:
            d=e
    for i in c[::-1]:
        if len(i)==d:
            print(i)
            break

        
