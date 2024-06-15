def  stuid(data2):
    n=len(data2)/10
    i=0
    ls=[]
    if i<n:
        i+=10
        for x in data2[i:i+7]:
            ls.append(x)
    return ls
        


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

