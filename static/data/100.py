count,sum = 0,0
while True:
    n = input()
    if n != '#':
        count+=1
        sum += int(n)  # 将用户输入的内容转换为整数再进行累加
    else:
        break
print(count,sum)


