student = eval(input())
info = str(student).split(",")[1:3]
avg = sum(student.split(",")[-1])/len(student.split(","))
print(info)
print("%.2f"%avg)

