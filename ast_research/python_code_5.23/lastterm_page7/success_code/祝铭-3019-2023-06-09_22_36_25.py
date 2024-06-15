li = input().split(' ')
lig = li[1:]
ligr = []
for i in lig:
    ligr.append(eval(i))
ligc = ligr[:]
a,b,c = ligc[0],ligc[1],ligc[2]
if b > a and b > c:
    a,b = b,a
    if c > b:
        b,c = c,b
if c > a and c > b:
    a,c = c,a
    if c > b:
        b,c = c,b
ligr = [a,b,c]
avg = sum(ligr)/len(ligr)
print('%s %.2f %.2f %.2f %.2f'%(li[0],ligr[0],ligr[1],ligr[2],avg))
