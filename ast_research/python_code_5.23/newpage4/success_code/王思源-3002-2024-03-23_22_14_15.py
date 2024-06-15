list = eval(input())

sum = 0.0
for i in range(len(list)):
    sum = sum + list[i]

avg = sum/len(list)
int_avg = int(avg)
if(avg-int_avg != 0):
    print("%.2f"%avg)
else:
    print(int_avg)
