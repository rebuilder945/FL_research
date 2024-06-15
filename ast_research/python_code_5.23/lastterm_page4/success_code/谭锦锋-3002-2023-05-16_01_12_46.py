l = eval(input())
sum = 0
for i in range(len(l)):
    sum+=l[i]
if sum%len(l)==0:
    avg = sum/len(l)
    print("%d"%avg)
else:
    avg = sum/len(l)
    print("%.2f"%avg)
