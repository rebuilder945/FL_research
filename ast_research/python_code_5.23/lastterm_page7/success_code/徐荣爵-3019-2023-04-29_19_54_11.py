stu = {}
name,mark1,mark2,mark3 = input().split()
stu = dict([('name',name),('english',mark1),('python',mark2),('math',mark3)])
stu['avg'] = stu.get('avg',0)+(int(mark1)+int(mark2)+int(mark3))/3
lst = list(stu.values())
print(lst[0],end = ' ')
lst2 = []
for i in range(1,4):
    lst2 += [int(lst[i])]
lst2.sort(reverse=True)
for i in lst2:
    print('%.2f'%i,end=' ')
print('%.2f'%lst[4],end = ' ')
