student = eval(input())
info = tuple(student)[1:3]
avg = sum(tuple(student)[5:])/len(tuple(student)[5:])
print(info)
print("%.2f"%avg)

