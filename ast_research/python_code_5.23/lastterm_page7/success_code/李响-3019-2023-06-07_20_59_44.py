stu={}
x = input().split()
stu['name'] = x[0]
stu['english'] = eval(x[1])
stu['python'] = eval(x[2])
stu['math'] = eval(x[3])
a = []
a.append(stu['english'])
a.append(stu['python'])
a.append(stu['math'])
a.sort()
stu["avg"] = (stu["english"]+stu["python"]+stu["math"])/3
print(stu['name'],end=' ')
for i in (range(len(a))-1):
    print('%.2f'%(a[i]),end=' ')
print('{:.2f}'.format(stu['avg']))
