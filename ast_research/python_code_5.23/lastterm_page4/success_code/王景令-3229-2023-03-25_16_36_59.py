a = eval(input())
c = []
d = ''
for i in a:
    if a.count(i) == 1:
        c.append(i)
if c == []:
    print('False')
else:
    for i in c:
        d +=  str(i)+','
d = d - ','
print(d)

       

