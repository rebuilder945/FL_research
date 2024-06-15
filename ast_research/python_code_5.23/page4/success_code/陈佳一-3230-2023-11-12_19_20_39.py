a=eval(input())
a.sort(reverse=True)
b=[]
for x in a:
    c=str(x)
    b.append(c)    #将排序后的数据字符串化后放入一个新列表
s=''
u=''
for y in b:
    s=str(s)+y
    u=u+str(0)
if s==u:
    s=0  #  防止出现000的结果
print(s)
