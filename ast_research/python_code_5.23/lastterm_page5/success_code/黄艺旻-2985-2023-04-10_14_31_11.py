student = eval(input())
info = (student.split(',')[1]),(student.split(',')[2])
avg = sum((student.split(','))[5:])/len((student.split(','))[5:])
print(info)
print("%.2f"%avg)

