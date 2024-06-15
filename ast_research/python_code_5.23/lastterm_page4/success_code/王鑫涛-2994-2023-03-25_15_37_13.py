a=input().split(',')
b=input().split(',')
if b[0] in list(range(len(a))):
    for i in range(b[1]):
        a.append(b[0])
    print(a)
else:
    print('error')

