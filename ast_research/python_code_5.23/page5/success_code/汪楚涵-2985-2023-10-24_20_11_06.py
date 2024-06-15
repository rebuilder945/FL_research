student = eval(input())
info = tuple(student[1]+student[2])
avg = (student[5][0]+student[5][1]+student[5][2])/len(student[5])
print(info)
print("%.2f"%avg)

