names = [x for x in input().split(',')]
scores = [int(x) for x in input().split(',')]
 
students = []
for i in range(len(names)):
     students.append([names[i], scores[i]])
 
students.sort(key=lambda x: x[1]) 
 
print(students)


