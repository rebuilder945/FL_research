a=eval(input())
b=[]
for num in a:
    if a.count(num)==1:
        b.append(num)
b.sort()
if b:
    print(','.join(str(i)for i in b))
else:
    print('False')

