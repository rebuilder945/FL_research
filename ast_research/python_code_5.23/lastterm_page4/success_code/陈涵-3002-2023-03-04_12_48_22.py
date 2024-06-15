n = eval(input(""))
average = sum(n)/len(n)
if average-int(average)==0:
    print(int(average))
else:
    print("%.2f"%(average))


