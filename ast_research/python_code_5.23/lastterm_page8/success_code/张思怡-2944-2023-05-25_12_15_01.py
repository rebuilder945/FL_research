def  stuid(data2):
        return [char[:8] for char in data2]


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

