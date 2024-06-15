s = input()
count = []
if s == '':
    print('None')
else:
    for i in s:
        if i not in count:
            count.append(str(i))
    for j in count:
        if s.count(j) == 1:
            print(j)
            break

