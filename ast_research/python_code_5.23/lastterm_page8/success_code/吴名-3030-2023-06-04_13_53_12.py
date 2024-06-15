names = input().split(',')
scores = input().split(',')

students = [[name, int(score)] for name, score in zip(names, scores)]
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)

