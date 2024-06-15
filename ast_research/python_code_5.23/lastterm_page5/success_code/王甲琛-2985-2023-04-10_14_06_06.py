student = eval(input())
info = (a for a in student if type(a)==int)
avg = mean(student)
print(info)
print("%.2f"%avg)

