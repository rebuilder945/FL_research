n = input()
a = 0 
b = 0
c = 0
d = 0
for x in n:
    if 'a'<=x<='z' or 'A'<=x<='Z':
        a+=1
    elif ord(x)==32:
        b+=1
    elif '0'<=x<='9':
        c+=1
    else:
        d+=1
print(a,b,c,d)

