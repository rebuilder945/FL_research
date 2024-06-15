def add_id(data2):
    corrected_ids = []

    for item in data2:
        if len(item) == 6 and item.startswith("20"):
            corrected_id = "20" + item
            corrected_ids.append(corrected_id)

    return corrected_ids


data1 = input("请输入一行错误学号，以空格分隔：").split()
result = add_id(data1)
for x in result:
    print(x, end=" ")
