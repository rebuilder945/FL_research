a = input()
b = input()
student = a.split(",")
score = b.split(",")
b =len(student)
d =[]
for x in range(b):
    d.append([student[x],int(score[x])])
d.sort(key = lambda x:x[1] )
print(d)
