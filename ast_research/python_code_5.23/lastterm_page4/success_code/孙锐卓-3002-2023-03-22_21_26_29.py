lst = input()
lst = eval(lst)
total = sum(lst)
avg = total / len(lst)
if avg % 1 == 0:
    print(int(avg))
else:  
    print("%.2f"%avg)
