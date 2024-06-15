a = eval(input())
c = []
for i in a:
    if a.count(i) == 1:
        c.append(i)
if c == []:
    print('False')
else:
    print(str(c))
       

