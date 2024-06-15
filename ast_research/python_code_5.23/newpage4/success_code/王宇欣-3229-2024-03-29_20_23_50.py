a = eval(input())
b = []
for i in range(len(a)):
    if a.count(a[i]) == 1:
        b.append(a[i])
if len(b) != 0:
    b.sort(reverse=True)
    for i in range(len(b)-1):
        print(b.pop(),end=',')
    print(b.pop())
else:
    print('False')
