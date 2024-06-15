def  stuid(data2):
    data = '20200001张三 20200002李四 20200003王麻子'
    def conver(data):
        s_list = [temp[:8] for temp in data.split(' ')]
        print(' '.join(s_list))
    conver(data)

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

