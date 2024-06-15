ll=eval(input())
ll.sort(key=int)
n=0
for i in ll:
    if ll.count(i)>1:
        pass
    else:
        print('i,')
        n=1
if n==1:
    print('\b')
else:
    print('False')

