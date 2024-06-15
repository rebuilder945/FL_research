s=input()
print(s)
ls=[]
for x in s:
    ls.append(x)
for x in range(len(ls)):
    if ord(ls[x])<=ord("Z") and ord(ls[x])>=ord("A"):
        ls[x]=chr(ord("Z")-(ord(ls[x])-ord("A")))
    if ord(ls[x])<=ord("z") and ord(ls[x])>=ord("a"):
        ls[x]=chr(ord("z")-(ord(ls[x])-ord("a")))
print(''.join(ls))

