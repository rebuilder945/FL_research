a=input()
b=[0,0,0,0,0]
for i in a:
    if '0'<=i<='9':
        b[0]=1
    elif 'a'<=i<='z':
        b[1]=1
    elif "A"<=i<="Z":
        b[2]=1
    elif len(a)>=8:
        b[3]=1
    else:
        b[4]=1
print(sum(b))


