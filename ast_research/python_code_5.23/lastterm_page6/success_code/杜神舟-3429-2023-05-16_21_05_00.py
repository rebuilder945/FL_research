aa=input()
a,b,c,d=0,0,0,0
for x in aa:
    if ord('a')-1<ord(x)<ord('z')+1:
        a+=1
    elif type(x)==' ':
        b+=1
    elif type(x)==int or type(x)==float:
        c+=1
    else:
        d+=1
print(a,b,c,d)


