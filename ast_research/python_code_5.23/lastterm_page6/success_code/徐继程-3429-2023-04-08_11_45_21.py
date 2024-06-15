a=input()
ying=0
kong=0
shu=0
other=0
for x in range(len(a)):
    i=a[x]
    if ord(i)>=ord('0') and ord(i)<=ord('9'):
        shu+=1
    elif ord(i)>=ord('a') and ord(i)<=ord('z'):
        ying+=1
    elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
        ying+=1    
    elif ord(i)==ord(' '):
        kong+=1
    else:
        other+=1
print('%d %d %d %d'%(ying,kong,shu,other))


