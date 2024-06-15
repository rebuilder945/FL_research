D={}
for i in range(26):
    D[(chr(ord('A')+i))]=chr(ord('A')+25-i)
    D[(chr(ord('a')+i))]=chr(ord('a')+25-i)
mima=input()
for i in mima:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        print(D[i],end='')
    else:
        print(i,end='')

