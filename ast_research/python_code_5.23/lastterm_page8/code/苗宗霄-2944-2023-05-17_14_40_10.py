def  stuid(data2):
    result = [] # 初始化空列表result
    for item in data: # 遍历列表中的每一个元素
          if len(item) == 8: # 判断该元素是否为学号，即长度是否为8位
              result.append(item) # 如果是学号，就将该元素加入到result列表中
        return result # 返回结果

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

