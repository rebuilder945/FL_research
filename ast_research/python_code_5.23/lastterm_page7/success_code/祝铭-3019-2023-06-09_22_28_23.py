li = input().split(' ')
lig = li[1:]
ligr = []
for i in lig:
    ligr.append(eval(i))
ligr.sort
avg = sum(ligr)/len(ligr)
print('%s %.2f %.2f %.2f %.2f'%(li[0],ligr[0],ligr[1],ligr[2],avg))
