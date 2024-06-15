def add_id(data2):
        result = []
        for item in data:
            if len(item) == 6 and item.isdigit() and item[:2] == "19":
                # 添加"20"前缀生成正确学号
                result.append("20" + item)
            else:
                # 不符合要求的原样输出
                result.append(item)
        return result


data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

