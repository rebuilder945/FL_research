a = eval(input())
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a.reverse())
    else:
        print('False')
