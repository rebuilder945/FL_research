ls = list(eval(input()))
sum = sum(ls)
len = len(ls)
if sum%len==0:
    print(int(sum/len)) 
else:
    print("%.2f"%(sum/len))

