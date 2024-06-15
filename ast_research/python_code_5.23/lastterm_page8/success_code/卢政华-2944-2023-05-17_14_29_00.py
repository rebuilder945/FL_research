def  stuid(data2):
        student_id = []
        for item in data2:
            if len(item) == 8 and item.isdigit():
                student_id.append(item)
        return student_id


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

