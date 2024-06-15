name,english,python,math=eval(input()).split()
avg=(english+python+math)/3
grade=[english,python,math]
grade.sort(reverse=True)
print(name,end='')
for i in grade:
    print('%.2f'%i)
print('%.2f'%avg)
