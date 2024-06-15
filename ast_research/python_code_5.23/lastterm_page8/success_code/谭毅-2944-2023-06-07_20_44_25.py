def  stuid(data2):
        student_id = []
        for d in data2:
            if len(d) == 8 and d.isdigit():
                student_id.append(d)
        return student_id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

