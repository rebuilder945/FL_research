def change(y,m,n):
    y[m],y[n]=y[n],y[m] #交换元素位置
    print(y)
y=input().split() #分隔并形成列表
m,n=input().split()
change(y,m,n)
