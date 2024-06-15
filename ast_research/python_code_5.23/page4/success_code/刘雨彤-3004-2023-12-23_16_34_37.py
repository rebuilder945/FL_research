records={}#创立空字典
#接收数据
while  True:
    record=input().strip()
    if record == "QUIT":
        break
    else:
        name,time_str=record.split(",")
#将时间统一以秒数表达
    hours,minutes,seconds=map(int,time_str.split(":"))
    total_seconds=hours*3600+minutes*60+seconds
#处理数据，并储存在字典中
    if name not in records:
        records[name]=total_seconds
    else:
        records[name]-=total_seconds
        records[name]=abs(records[name])
#将结果按照总时间降序排列，并在总时间相同时按姓名降序排列
    sorted_times = sorted(records.items(),key=lambda x:x[1],reverse=True)
    sorted_times = sorted(records.items(),key=lambda x:x[0],reverse=True)
    sorted_times = sorted(records.items(),key=lambda x:len(x[0]))
   
#输出结果
for name,total_seconds in sorted_times:
    print(f"{name},{total_seconds}")

