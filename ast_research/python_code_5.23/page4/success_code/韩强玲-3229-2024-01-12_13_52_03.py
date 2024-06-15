a = eval(input())
b = []
for i in a:
    if a.count(i)==1:
        b.append(i)
        print(i,end=',')
if len(b)==0:
    print('False')
