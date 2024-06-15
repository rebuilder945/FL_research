a = input()
b = 1
for i in a:
    if a.count(i) == 1:
        b = 0
        print(i)
        break
if b == 1:
    print('None')
