student = eval(input())
info = tuple(student.split(",")[1])
avg = sum([x for x in student][5])/len([x for x in student][5])
print(info)
print("%.2f"%avg)

