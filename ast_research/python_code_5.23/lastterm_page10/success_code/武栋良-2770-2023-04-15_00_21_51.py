a = input()
b = input()
c = set(a)
for x in c:
    if a.count(x)!=b.count(x):
        print('False')
        break
else:
    print('True')

    

