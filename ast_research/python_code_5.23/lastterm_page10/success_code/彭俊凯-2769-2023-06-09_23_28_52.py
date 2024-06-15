a=list(input())
d=a[:]
b=[]
c=[]
for i in range(26):
    b.append(chr(ord('a')+i))
    c.append(chr(ord('A')+i))
for i in range(len(a)):
    if a[i] in b:
        a[i]=chr(26-(ord(a[i])-ord('a')+1)+ord('a'))
    elif a[i] in c:
        a[i]=chr(26-(ord(a[i])-ord('A')+1)+ord('A'))
print("".join(d))
print("".join(a))

