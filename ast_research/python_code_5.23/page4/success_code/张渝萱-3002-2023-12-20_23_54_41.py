a = eval(input())
count = 0
k = 0
for x in a:
    k += x
    count += 1
average = k/count
b = average - int(average)
if b==0:
    print(int(average))
else:
    print("%.2f" % average)
