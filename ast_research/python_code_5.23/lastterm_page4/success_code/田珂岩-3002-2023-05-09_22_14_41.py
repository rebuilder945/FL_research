ls = eval(input())
avg = sum(ls)/len(ls)
if type(avg) == int:
    print(avg)
else:
    print("{:.2f}".format(avg))    

