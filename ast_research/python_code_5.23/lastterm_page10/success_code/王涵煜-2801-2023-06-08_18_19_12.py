a=input()
c=[0,0,0,0,0]
for i in a:
    if '0'<=i<='9':
        c[0]=1
    if 'a'<=i<='z':
        c[1]=1
    if 'A'<=i<='Z':
        c[2]=1
    if i in '~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\': 
        c[3]=1
    if len(a)>=8:
        c[4]=1
print(c.count(1))

