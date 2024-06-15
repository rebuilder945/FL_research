student = eval(input())
info =   tuple(student[1:3])
avg = sum(student[4:5])/len(student[4:5])
print(info)
print("%.2f"%avg)

