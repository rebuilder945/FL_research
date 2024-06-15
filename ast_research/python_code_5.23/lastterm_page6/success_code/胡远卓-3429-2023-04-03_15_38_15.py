s=input()
L=len(s)
a,b,c,d=0,0,0,0
for i in range(L):
    if ord(s[i])>=ord('a') and ord(s[i])<=ord('z'):
        a+=1
    elif ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
        a+=1
    elif ord(s[i])>=ord('0') and ord(s[i])<=ord('9'):
        c+=1
    elif s[i]==' ':
        b+=1
    else:
        d+=1
print("%d %d %d %d"%(a,b,c,d))
