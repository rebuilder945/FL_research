D={}
for i in range(26):
    D[chr(ord('A')+i)]=chr(ord('A')+25-i)
    D[chr(ord('a')+i)]=chr(ord('a')+25-i)
s=input()
f=""
for i in s:
    if i.isalpha():
        f+=D[i]
    else:
        f+=i
print(s)
print(f)
