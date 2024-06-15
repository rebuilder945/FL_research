a = input().split(',')
c,b = eval(input())

if c>=0:
    if c>len(a)-1 or c<-len(a):
        print('error')
    elif c==len(a)-1:
        copy = a[c:]
        for k in range(b):
            a.extend(copy)
        for i in range(len(a)):
            a[i] = int(a[i])
        print(a)
    else:
        copy = a[c:c + 1]
        for k in range(b):
            a.extend(copy)
        for i in range(len(a)):
            a[i] = int(a[i])
        print(a)
elif c<0:
    if c<-len(a):
        print('error')
    elif c==len(a)-1:
        copy = a[c-1:c]
        for k in range(b):
            a.extend(copy)
        for i in range(len(a)):
            a[i] = int(a[i])
        print(a)
    else:
        copy = a[c-1:c]
        for k in range(b):
            a.extend(copy)
        for i in range(len(a)):
            a[i] = int(a[i])
        print(a)
