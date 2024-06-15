count=0
sum=0
while 1:
    a=input()#表示输入
    if a=='#':
        break#跳出循环
    count=count+1
    sum=sum+int(a)
print(count,sum)
