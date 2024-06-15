total = 0 #整数总和
count = 0 #数量总和
 
while True: #无限循环
    integer = input() #请求输入
 
    if integer == "#":
        break #跳出循环
    
    total += int(integer)
    count += 1
 
print(count, total)

