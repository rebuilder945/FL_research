list = eval(input())
a = sum(list)
average = a/len(list)
if average%1 == 0:
    print(int(average))
else:
    print("%.2f"%(average))
