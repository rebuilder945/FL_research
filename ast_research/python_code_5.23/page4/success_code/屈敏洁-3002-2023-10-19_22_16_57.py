ls = eval(input())
total = 0
for num in ls:
    total += num
average = total / len(ls)    
if average % 1:
    print("%.2f"%(average))
else:
    print("%d"%(average))   
