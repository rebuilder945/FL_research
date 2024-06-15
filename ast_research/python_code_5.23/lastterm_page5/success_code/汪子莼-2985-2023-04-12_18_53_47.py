student = eval(input())
info = tuple(student[1:3])
avg = tuple(sum(student[-1]).split()/3)
print(info)
print("%.2f"%avg)

