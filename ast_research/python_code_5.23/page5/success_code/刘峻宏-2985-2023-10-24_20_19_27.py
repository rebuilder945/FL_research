student = eval(input())
info = student[1:3]
avg = sum(str(student).split(",")[-1])/len(str(student).split(",")[-1])
print(info)
print("%.2f"%avg)

