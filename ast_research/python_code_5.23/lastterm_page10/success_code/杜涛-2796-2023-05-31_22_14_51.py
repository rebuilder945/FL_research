a=input()
for i in a:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        b=a.replace(i,' ')
        a=b
c=list(a.strip().split())
d=0
for i in c:
    e=len(i)
    if e>d:
        d=e
for i in c[::-1]:
    if len(i)==d:
        print(i)
        break

        
