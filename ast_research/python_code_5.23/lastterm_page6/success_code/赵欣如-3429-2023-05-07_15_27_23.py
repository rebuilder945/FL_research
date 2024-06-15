def yingwen(n):
    if (ord(n)>64 and ord(n)<91)or(ord(n)>96 and ord(n)<123):
        return True
def kongge(n):
    if ord(n)==32:
        return True
def shuzi(n):
    if ord(n)>47 and ord(n)<58:
        return True
def qita(n):
    if (ord(n)>32 and ord(n)<48)or(ord(n)>57 and ord(n)<65)or(ord(n)>90 and ord(n)<97)or(ord(n)>122 and ord(n)<127):
        return True
m=str(input())
a=0
b=0
c=0
d=0
for i in m:
    if yingwen(i):
        a+=1
    if kongge(i):
        b+=1
    if shuzi(i):
        c+=1
    if qita(i):
        d+=1
print(a,b ,c ,d,end=" ")

