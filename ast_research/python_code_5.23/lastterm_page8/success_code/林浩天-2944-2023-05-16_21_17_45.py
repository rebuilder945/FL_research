def  stuid(data2):
    s_list = [temp[:8] for temp in data2]
    return s_list


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

