sb = eval(input())
b = []
for i in sb:
    x = sb.count(i)
if x==1:
    b.append(i)
print(','.join(map(str,b)))
if sum(b)==0:
    print('False')
