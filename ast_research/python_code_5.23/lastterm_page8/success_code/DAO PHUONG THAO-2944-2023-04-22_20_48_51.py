def  stuid(data2):
        stuid_list = []
        i = 0
        while i < len(data):
            if data[i:i+8].isdigit():
                stuid_list.append(data[i:i+8])
                i += 8
            else:
                i += 1
        return ' '.join(stuid_list)


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

