a = input()
b = input()
student = a.split(",")
score = b.split(",")
b =len(student)
d =[]
for x in range(b):
    d.append([student[x],score[x]])
print(d)
