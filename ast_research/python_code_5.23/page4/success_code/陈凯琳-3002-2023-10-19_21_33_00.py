lit=eval(input())
a=0
for i in range(len(lit)):
    a+=lit[i]
av=a/len(lit)
if int(av)==av:
    print(int(av))
else:
    print('%.2f'%av)
