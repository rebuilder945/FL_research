student = eval(input())
info = tuple(str(student[1]+student[2]).split())
avg = sum(student[5])/len(student[5])
print(info)
print("%.2f"%avg)

