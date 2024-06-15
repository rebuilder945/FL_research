def  stuid(data2):
        student_ids = [item for item in data2 if len(item) == 8 and item.isdigit()]
        return student_ids


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

