name,*grade=input().split()
grade=list(map(int,grade))
avg=sum(grade)/3
grade.sort(reverse=True)
print(name,end='')
for i in grade:
    print('%.2f'%i)
print('%.2f'%avg)
