a=input().split(',')
b=input().split(',')
if b[0] in range(len(a)-1):
    for i in range(b[1]):
        a.append(b[0])
    print(a)
else:
    print('error')

