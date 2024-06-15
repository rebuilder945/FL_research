a=input().split(' ')
if int(a[1])<int(a[2]):
    a[1],a[2]=a[2],a[1]
if int(a[2])<int(a[3]):
    a[2],a[3]=a[3],a[2]
if int(a[1])<int(a[2]):
    a[1],a[2]=a[2],a[1]
ave='%.2f'%((int(a[1])+int(a[2])+int(a[3]))/3)
a.append(ave)
print(a[0],'%.2f'%int(a[1]),'%.2f'%int(a[2]),'%.2f'%int(a[3]),a[4])
