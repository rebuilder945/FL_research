a1 = input().split(',')
b,c=eval(input())
a = []
for i in range(len(a1)):
    a.append(eval(a1[i]))
if b >= len(a):
    print('error')
else:
    for i in range(c):
        a.append(a[b])
    print(a)
