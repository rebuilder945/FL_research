#a=list(map(int,input().split(",")))#split其实是在提醒map和list：，不是元素
#数字限定使用
a=list(eval(input()))
b=[]
b.append(a[0])
for i in range(a[1]-1):
    d=int(a[2])
    c=int(a[2])+int(a[0])
    f=c+i*d
    b.append(f)
print(b)
