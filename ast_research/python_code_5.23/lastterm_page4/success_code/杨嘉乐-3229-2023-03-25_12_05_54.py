ll=eval(input())
ll.sort(key=int)
n=0
lll=[]
for i in ll:
    if ll.count(i)>1:
        pass
    else:
        lll.append(i)
        n=1
if n==1:
    print(','.join(str(i) for i in lll))
else:
    print('False')

