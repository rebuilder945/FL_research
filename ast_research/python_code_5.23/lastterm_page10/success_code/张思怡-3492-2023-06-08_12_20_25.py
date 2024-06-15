a=input()


for i in range(len(a)):
    if i ==0:
        if a[0]not in a[1:]:
            print(a[0])
    else:
        b=a[(i+1):]
        c=a[:(i-1)]
        if (a[i] not in b )and (a[i]not in c):
            print(a[i])
            break
