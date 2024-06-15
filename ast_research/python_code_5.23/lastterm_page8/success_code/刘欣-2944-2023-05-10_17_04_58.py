def  stuid(data2):
        stu_id = []  
        for data in data2:  
            if len(data) == 8: 
                stu_id.append(data) 
        return stu_id 

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

