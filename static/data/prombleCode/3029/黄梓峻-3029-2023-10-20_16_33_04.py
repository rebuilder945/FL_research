name_list=input().split(',')
grades_list=eval(input())
output1=[]
for i in range(len(name_list)):
    output=(name_list[i],grades_list[i])
    output1.append(list(output))
print(output1)
