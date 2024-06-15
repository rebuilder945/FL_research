a=input().split()
dic={}
dic['name']=a[0]
dic['english']=a[1]
dic['python']=a[2]
dic['math']=a[3]
average=(eval(a[1])+eval(a[2])+eval(a[3]))/3
dic['avg']=average
lst =[]
for x in range(1,4):
    t=a[x]
    lst.append(t)
lst.sort()
a =lst[0]
b=lst[1]
c=lst[2]
print(dic['name'],'%.2f'%eval(str(a)),'%.2f'%eval(str(b)),'%.2f'%eval(str(c)),'%.2f'%eval(str(dic['avg'])))

