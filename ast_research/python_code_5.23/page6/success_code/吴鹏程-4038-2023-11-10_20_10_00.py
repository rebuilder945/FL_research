n=input()
a,s,c,d=0,0,0,0
for i in n:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        a+=1
    elif i==" ":
        s+=1
    elif '0'<=i<='9':
        c+=1
    else:
        d+=1
print(a,s,c,d)


