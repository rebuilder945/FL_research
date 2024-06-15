string=input()
a,b,c,d=(0,0,0,0)
for x in string:
    if 'a'<=x<='z' or 'A'<=x<='Z':
        a+=1
    elif x==' ':
        b+=1
    elif '0'<=x<='9':
        c+=1
    else: d+=1
print(a,b,c,d)
