a=input()
if a=='':
    print('None')
for i in range(len(a)):
    if i ==0:
        if a[0]not in a[1:]:
            print(a[0])
            break
    else:
        b=a[(i+1):]
        c=a[:i]
        if (a[i] not in b )and (a[i]not in c):
            print(a[i])
            break
        
