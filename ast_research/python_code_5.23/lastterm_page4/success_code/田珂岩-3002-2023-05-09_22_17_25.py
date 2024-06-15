ls = eval(input())
avg = sum(ls)/len(ls)
if (avg*10) % 10 == 0:
    print(avg)
else:
    print("{:.2f}".format(avg))    

