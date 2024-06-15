# 把姓名和成绩列表合并后按照成绩升序排列
a=input().split(',')
b=input().split(',')
c=[]
for i in range(0,len(a)):
    c.append([a[i],int(b[i])])
c.reverse()
c.sort()
print(c)
