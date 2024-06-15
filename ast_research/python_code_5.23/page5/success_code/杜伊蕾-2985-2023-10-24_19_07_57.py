student = eval(input())
info = tuple(student[1:3])
avg = sum(int(str(student[-1])))/len(str(student[-1]))
print(info)
print("%.2f"%avg)

