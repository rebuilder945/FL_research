m=input()
a=[0,0,0,0,0]
c=0
for i in m:
    if i.isdigit():
        a[0]=1
    elif 'a'<=i<='z':
        a[1]=1     
    elif 'A'<=i<='Z':
        a[2]=1
    elif i in '~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\':
        a[3]=1
    elif len(m)>=8:
        a[4]=1
for x in a:
    if x==1:
        c+=1
print(c)
