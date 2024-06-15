names=list(input().split(","))
grades=list(eval(input()))
# a=[[x+','+str(y)] for x in names for y in grades]
name_grade = []
for i in range(len(names)):
    name_grade.append([names[i],(grades[i])])
print(name_grade)
