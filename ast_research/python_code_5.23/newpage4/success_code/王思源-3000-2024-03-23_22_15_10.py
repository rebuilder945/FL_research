list = eval(input())

sum = 0.0
for i in range(len(list)):
    sum = sum + list[i]

avg = sum/len(list)
print("%.2f"%avg)


