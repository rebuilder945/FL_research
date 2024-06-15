a=str(input())
b=str(input())
c=1
for i in a:
    if a.count(i)!=b.count(i):
        c=0
if c :
    print('True')
else:
    print('Folse')
