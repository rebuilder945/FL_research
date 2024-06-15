def  stuid(data2):
        student_id = []
        for item in data2:
            # 判断每个字符串是否是8位的数字，如果是，则添加到学号列表中
            if item.isdigit() and len(item) == 8:
                student_id.append(item)
        return student_id


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

