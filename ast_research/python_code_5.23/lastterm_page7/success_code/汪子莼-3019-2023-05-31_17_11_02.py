name,*grade=input().split()
grade=list(map(int,grade))
avg=sum(grade)/len(grade)
grade.sort()
print('%s'%name,end=' ')
for i in grade:
    print('%.2f'%i,end=' ')
print('%.2f'%avg,end='')
