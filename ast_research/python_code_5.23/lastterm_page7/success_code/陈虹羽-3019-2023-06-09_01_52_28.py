stu={}
a=input().split()
stu['name']=a[0]
stu['english']=a[1]
stu['python']=a[2]
stu['math']=a[3]
b=(int(a[1])+int(a[2])+int(a[3]))/3
t=a[1:]
for i in range(len(t)):
    t[i]=int(t[i])
t.sort(reverse=True)
t.append(b)
print(a[0],end=' ')
for i in t:
    print('%.2f'%(int(i)),end=' ')

