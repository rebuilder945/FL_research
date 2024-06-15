a=input()
b=[0,0,0,0,0]
if len(a)>=8:
    b[3]=1
for i in a:
    if 'A'<=i<='Z':
        b[0]=1
    elif 'a'<=i<='z':
        b[1]=1
    elif '1'<=i<='9':
        b[2]=1
    elif i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
        b[4]=1
print(sum(b))
