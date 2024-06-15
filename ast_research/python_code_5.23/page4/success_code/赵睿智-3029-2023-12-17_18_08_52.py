# 定义函数将时间字符串转换为秒数  
def time_to_seconds(time_str):  
    return int(time_str.split(':')[0]) * 3600 + int(time_str.split(':')[1]) * 60 + int(time_str.split(':')[2])  
  
# 定义函数计算锻炼时长  
def calculate_duration(name, data):  
    # 初始化进场时间和出场时间  
    enter_time = None  
    leave_time = None  
    # 遍历所有时间记录，找出进场和出场时间  
    for time in data:  
        if enter_time is None and leave_time is None:  
            enter_time = time  
        elif enter_time is not None and leave_time is None:  
            leave_time = time  
        else:  
            break  # 如果已经找到进场和出场时间，就退出循环  
    # 计算锻炼时长（忽略可能的多次进出）  
    if enter_time is not None and leave_time is not None:  
        duration = leave_time - enter_time  
    else:  
        duration = 0  # 如果找不到进场或出场时间，锻炼时长为0  
    return duration  
  
# 主程序开始  
data = {}  # 用字典来存储每个学生的锻炼数据  
while True:  
    line = input().strip()  # 从标准输入读取一行数据  
    if line == 'QUIT':  # 如果输入QUIT，就退出循环  
        break  
    name, time = line.split(',')  # 将姓名和时间从输入行中分割出来  
    if name not in data:  # 如果该学生还未在字典中，就初始化他的数据列表  
        data[name] = []  
    data[name].append(time_to_seconds(time))  # 将时间转换为秒数并添加到该学生的数据列表中  
  
# 计算每个学生的锻炼时长并按照要求排序结果  
result = []  
for name, data in sorted(data.items(), key=lambda x: (-sum(x[1]), x[0])):  # 先按锻炼时长降序排序，时长相同则按姓名降序排序  
    result.append((calculate_duration(name, data), name))  # 计算每个学生的锻炼时长并添加到结果列表中  
result.sort(reverse=True)  # 再按锻炼时长降序排序整个结果列表  
  
# 输出结果  
for duration, name in result:  
    print(f'{name},{duration}')  # 输出姓名和锻炼时长，以逗号分隔，时长以秒为单位


