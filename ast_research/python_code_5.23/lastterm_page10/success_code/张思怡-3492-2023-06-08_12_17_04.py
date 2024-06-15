a=input()

# print(a[1:])
for i in range(len(a)):
    b=a[(i+1):]
    c=a[:(i-1)]
    if (a[i] not in b )and (a[i]not in c):
        print(a[i])
        break
