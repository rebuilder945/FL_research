sum=0 #整数总和
count=0 #数量总和
while True: #无限循环
    a=input() #请求输入
    if a == "#":
        break #跳出循环
    sum+= int(a)
    count += 1
print(count, sum)



