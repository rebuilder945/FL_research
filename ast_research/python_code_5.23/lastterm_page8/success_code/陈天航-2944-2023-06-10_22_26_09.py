def  stuid(data2):
            a=" ".join(data2)
            for i in  a:
                if i.isspace() or i.isdigit():
                        a=a
                else:
                      a=a.replace(i,"") 
            return a.split(" ")

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

