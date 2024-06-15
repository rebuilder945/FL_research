aa=input()
a,b,c,d=0,0,0,0
for x in aa:
    if ord('a')-1<ord(x)<ord('z')+1 or ord('A')-1<ord(x)<ord('Z')+1:
        a+=1
    elif x==' ':
        b+=1
    elif ord('0')-1<ord(x)<ord('9')+1:
        c+=1
    else:
        d+=1
print(a,b,c,d)



