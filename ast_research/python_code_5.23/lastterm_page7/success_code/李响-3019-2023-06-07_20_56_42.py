stu={}
stu['name'] = input()
stu['english'] = eval(input())
stu['python'] = eval(input())
stu['math'] = eval(input())
a = []
a.append(stu['english'])
a.append(stu['python'])
a.append(stu['math'])
a.sort()
stu["avg"] = (stu["english"]+stu["python"]+stu["math"])/3
print(stu['name'],end=' ')
for i in range(len(a))-1:
    print('%.2f'%(a[i]),end=' ')
print('{:.2f}'.format(stu['avg']))
