student = eval(input())
info = tuple(x for x in student(1,3))
avg = sum(student[-1])/len(student[-1])
print(info)
print("%.2f"%avg)

