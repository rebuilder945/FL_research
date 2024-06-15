n=input()
m=input()
for x in n:
    if n.count(x)!=m.count(x):
        print('False')
else:
    print('True')
