def add_id(data2):
    
    result = []
    for x in data2:
        if len(x) == 6 and x.isdigit():
                # 如果输入的学号长度为6且全部由数字组成，则进行转换
            result.append('20' + x)
    else:
                # 否则直接将该学号加入结果列表
        result.append(x)
    return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

