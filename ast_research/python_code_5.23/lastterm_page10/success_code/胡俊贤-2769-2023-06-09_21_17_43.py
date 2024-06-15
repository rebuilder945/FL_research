D={}
for i in range(26):
    D[chr(ord('a')+i)]=chr(ord('a')+25-i)
    D[chr(ord('A')+i)]=chr(ord('A')+25-i)
s=input()
c=''
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        c+=D[i]
    else:
        c+=i
print(c)


