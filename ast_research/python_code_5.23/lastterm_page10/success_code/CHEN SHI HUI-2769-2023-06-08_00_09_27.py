
d={}
for i in range(26):
    d[chr(ord('A')+i)]=chr(ord('Z')-i)
    d[chr(ord('a')+i)]=chr(ord('z')-i) 
a=input()
c=''
for i in a:
    if i.isalpha():
        c+=d[i]
    else:
        c+=i
print(a)
print(c)
