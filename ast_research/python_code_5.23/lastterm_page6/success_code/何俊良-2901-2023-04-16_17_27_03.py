total_sum = 0
count = 0

while True:
    try:
        data = input()
        # 如果输入为 #，则退出循环
        if data == "#":
            break

        # 如果输入不是数字，则忽略本次输入
        value = int(data.strip())

        count += 1
        total_sum += value

    except ValueError:
        continue


result = '{} {}'.format(count, total_sum)
print(result)

