s=input()
w=0
b=0
n=0
o=0
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        w+=1
    elif '0'<=i<='9':
        n+=1
    elif i==" ":
        b+=1
    else:
        o+=1
print(w,b,n,o)
