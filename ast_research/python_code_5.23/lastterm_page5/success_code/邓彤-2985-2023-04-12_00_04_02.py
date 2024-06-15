student = eval(input())
info = tuple(student[1:3])
avg = sum([x for x in student][5])/len([x for x in student][5])
print(info)
print("%.2f"%avg)

