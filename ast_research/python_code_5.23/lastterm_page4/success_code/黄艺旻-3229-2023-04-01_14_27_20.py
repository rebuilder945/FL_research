a = eval(input())
for i in range(len(a)):
    if a.counter(a[i]) == 1:
        print(a.reverse())
    else:
        print('False')
