s = eval(input())
sum = sum(s)
avg = sum/len(s)
if type(avg) is type(1):
    print(int(avg))
else:
    print("%.2f"%avg)
