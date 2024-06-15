a = input().split()
stu={}
stu['name']=a[0]
stu['english']=eval(a[1])
stu['python']=eval(a[2])
stu['math']=eval(a[3])
stu['avg']=sum(list(map(int,a[1:])))/len(a[1:])
save=list(stu.values())
print(save[0],end=" ")
t = save[1:4]
t.sort()
t.reverse()
print('%.2f'%t[0],end=" ")
print('%.2f'%t[1],end=" ")
print('%.2f'%t[2],end=" ")
print('%.2f'%save[-1])

