def  stuid(data2):
        student_id = []
        for x in data2: 
            student_id.append(x[:8]) 
        return student_id 
        return student_id


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

