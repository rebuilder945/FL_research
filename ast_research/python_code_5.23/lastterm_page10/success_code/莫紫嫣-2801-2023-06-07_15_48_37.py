a=input()
b=[0,0,0,0,0]
for i in a:
    if '0'<=i<='9':
        b[0]=1
    if 'a'<=i<='z':
        b[1]=1
    if 'A'<=i<='Z':
        b[2]=1
    if i in "~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\":
        b[4]=1
if len(a)>=9:
    b[3]=1
print(a.count(1))
