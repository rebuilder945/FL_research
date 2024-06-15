list = eval(input())
a = sum(list)
average = eval(a/len(list))
if type(average) == int:
    print("average")
else:
    print("%.2f"%(average))
