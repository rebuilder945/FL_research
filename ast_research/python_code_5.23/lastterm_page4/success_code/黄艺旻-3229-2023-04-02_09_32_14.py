a = eval(input())
b = []
for i in range(len(a)):
    if a.counter(a[i]) == 1:
        b.append(a[i])
        print(b)
    else:
        print('False')
