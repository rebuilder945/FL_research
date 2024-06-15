names = input().split(",")
scores = list(map(int, input().split(",")))
student_list = [[name, score] for name, score in zip(names, scores)]
sorted_list = sorted(student_list, key=lambda x: x[1])
print(sorted_list)
